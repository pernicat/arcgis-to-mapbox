"""tool for downloading from arcgis feature server"""
import functools
import io
import json
import logging
import time
import typing as t

import requests
import click

from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# logger.setLevel(logging.INFO)


DEFAULT_WAITS = [1, 2, 5, 8, 15, 30, 600]


class RequestError(Exception):
    """Request Failure exception"""


class NotJSONError(Exception):
    """The result is not json"""


def iterable_to_stream(iterable: t.Iterable, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    Lets you use an iterable (e.g. a generator) that yields bytestrings as a read-only
    input stream.

    The stream implements Python 3's newer I/O API (available in Python 2's io module).
    For efficiency, the stream is buffered.

    https://stackoverflow.com/questions/6657820/how-to-convert-an-iterable-to-a-stream/20260030#20260030
    """
    class IterStream(io.RawIOBase):
        """Subclass for turing an iterator into a stream"""
        def __init__(self):
            self.leftover = None
        def readable(self):
            return True
        def readinto(self, b):
            try:
                l = len(b)  # We're supposed to return at most this much
                chunk = self.leftover or next(iterable)
                output, self.leftover = chunk[:l], chunk[l:]
                b[:len(output)] = output
                return len(output)
            except StopIteration:
                return 0    # indicate EOF
    return io.BufferedReader(IterStream(), buffer_size=buffer_size)


def _try_request_repeater(f: callable, waits: t.Iterable = None):
    """trys to run a request muliple times"""
    waits = waits or DEFAULT_WAITS

    for wait in waits:
        try:
            return f()
        except RequestError as e:
            logger.warning("request failed '%s', waiting for %d seconds", str(e), wait)
            time.sleep(wait)
    logging.critical("multiple failures, shutting down...")
    raise Exception("Multiple failures")


def check_response(response: requests.Response) -> t.Optional[t.Mapping]:
    """check if a reponse is valid and raises an exception if it is not"""
    if not response.ok:
        message = (
            f"status_code={response.status_code}, url={response.url} body='{response.text}'"
        )
        logger.error(message)
        raise RequestError(message)

    try:
        if not response.text:
            return None
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        logger.error("error decoding response '%s'", response.text)
        raise NotJSONError from e



class ArcGISQuery:
    """wrapper for querying an ArgGIS service"""

    def __init__(self, service: "ArcGISService", where: str):
        self.service = service
        self.where = where

    def query_request(self, params: t.Mapping) -> t.Mapping:
        """gets a json response with the specified parameters"""
        response = requests.get(
            self.service.query_url,
            params={
                "f": "json",
                "where": self.where,
                **params,
            },
        )
        check_response(response)

        return response.json()

    @functools.cached_property
    def count_extent(self) -> t.Mapping:
        """retursn the count and extent information"""
        return self.query_request({
            "returnCountOnly": "true",
            "returnExtentOnly": "true",
        })

    @property
    def extent(self) -> t.Mapping:
        """gets the extent info"""
        return self.count_extent["extent"]

    @property
    def count(self) -> int:
        """gets the result count of the query"""
        return self.count_extent["count"]

    def geojson_range(self, offset: int, count_: int) -> t.Mapping:
        """queries the FeatureServer"""
        return self.query_request({
                "f": "geojson",
                "outFields": "*",
                "resultOffset": offset,
                "resultRecordCount": count_,
                "where": self.where,
        })

    @property
    def geojson_parts(self) -> t.Generator[t.Mapping, None, None]:
        """returns all Features from the query"""
        for offset in range(0, self.count, self.service.max_record_count):
            logging.info(
                "importing: %d/%d (%.2f%%)",
                offset,
                self.count,
                100 * offset / self.count,
            )
            yield _try_request_repeater(
                functools.partial(
                    self.geojson_range, offset, self.service.max_record_count
                )
            )

    @property
    def features(self) -> t.Generator[t.Mapping, None, None]:
        """reaturns all features from multiple queries as a generator"""
        for feature_collection in self.geojson_parts:
            if not feature_collection["features"]:
                raise Exception("no more 'features'")

            yield from feature_collection["features"]

    @property
    def feature_strings(self) -> t.Generator[str, None, None]:
        """converts the features into strings"""
        for feature in self.features:
            yield json.dumps(feature) + "\n"


class ArcGISService:
    """for getting data from an ArcGIS Feature server"""

    def __init__(self, service_url: str, service_layer: int = 0):
        self._service_url = service_url
        self._service_layer = service_layer

    @property
    def query_url(self) -> str:
        """the url for running queries"""
        return f"{self._service_url}/{self._service_layer}/query"

    @functools.cached_property
    def info(self) -> t.Mapping:
        """gets information about the service"""
        r = requests.get(self._service_url, params={"f": "json"})

        assert r.status_code == 200

        return r.json()

    @property
    def max_record_count(self) -> int:
        """the maximum records that can be returned per requests"""
        return self.info["maxRecordCount"]

    @property
    def size(self) -> int:
        """the total size of the dataset"""
        return self.info["size"]


class MapboxTilesetSource:
    """api adapter for mapbox source"""

    API_URL = "https://api.mapbox.com"

    def __init__(self, user: str, access_token: str):
        self.user = user
        self._access_token = access_token

    @property
    def url(self):
        """gets the tileset service url"""
        return f"{self.API_URL}/tilesets/v1/sources/{self.user}"

    @property
    def list(self) -> t.Collection:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#example-request-list-tileset-sources
        """
        response = requests.get(
            f"{self.url}", params={"access_token": self._access_token}
        )
        return check_response(response)

    def delete(self, id_: str) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#delete-a-tileset-source
        """
        response = requests.delete(f"{self.url}/{id_}", params={"access_token": self._access_token})
        return check_response(response)

    def upload(self, id_: str, fp: t.TextIO) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset
        """
        response = requests.post(
            f"{self.url}/{id_}",
            files={"file": fp},
            params={"access_token": self._access_token}
        )
        return check_response(response)


class MapboxTileset:
    """api adapter for mapbox source"""

    API_URL = "https://api.mapbox.com"
    VALID_PROPERTIES = {
        "recipe": t.Mapping,
        "name": str,
        "private": bool,
        "description": str,
        "attribution": t.List,
        # "attribution.text": str,
        # "attribution.link": str,
    }

    def __init__(self, name: str, access_token: str):
        self.name = name
        self._access_token = access_token

    @property
    def url(self):
        """gets the tileset service url"""
        return f"{self.API_URL}/tilesets/v1/{self.name}"

    def _check_parameters(self, **kvargs) -> t.Mapping:
        """checks the parameters to make sure they are valid"""
        if "recipe" not in kvargs:
            raise Exception("'recipe' is a required property")

        for key, value in kvargs.items():
            if key not in self.VALID_PROPERTIES:
                raise Exception(f"'{key}' is not a valid property")

            if not isinstance(value, self.VALID_PROPERTIES[key]):
                raise Exception(f"'{key}' is an invalid type")

        data = {
            "name": self.name,
            **kvargs,
        }

        logger.debug(data)

        return data

    def create(self, **kvargs) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#create-a-tileset

        Args:
            recipe (t.Mapping):
                A recipe that describes how the GeoJSON data you
                uploaded should be transformed into tiles.
            name (str):
                The name of the tileset. Limited to 64 characters.
            private (bool):
                Describes whether the tileset must be used with an
                access token from your Mapbox account.
            description (str):
                A description of the tileset. Limited to 500 characters.
                attributes (t.List[t.Mapping[str, str]]): An array of attribution objects,
                each with text and link keys. Limited to three attribution objects, 80
                characters maximum combined across all text values, and 1000 characters
                maximum combined across all link values.
        """
        data = self._check_parameters(**kvargs)

        response = requests.post(
            self.url,
            json=data,
            params={"access_token": self._access_token}
        )
        return check_response(response)
    
    def update(self, **kvargs) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#update-tileset-information
        """
        data = self._check_parameters(**kvargs)

        response = requests.patch(
            self.url,
            json=data,
            params={"access_token": self._access_token},
        )
        return check_response(response)


    def update_recipe(self, recipe: t.Mapping) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#update-a-tilesets-recipe
        """
        response = requests.patch(
            f"{self.url}/recipe",
            json=recipe,
            params={"access_token": self._access_token},
        )
        return check_response(response)


    def publish(self) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#publish-a-tileset
        """
        response = requests.post(
            f"{self.url}/publish",
            params={"access_token": self._access_token},
        )
        return check_response(response)

    def jobs(self) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#list-information-about-all-jobs-for-a-tileset
        """
        response = requests.get(
            f"{self.url}/jobs",
            params={"access_token": self._access_token}
        )
        return check_response(response)

    def job_status(self, job_id: str) -> t.Mapping:
        """
        https://docs.mapbox.com/api/maps/mapbox-tiling-service/#retrieve-information-about-a-single-tileset-job
        """
        response = requests.get(
            f"{self.url}/jobs/{job_id}",
            params={"access_token": self._access_token}
        )
        return check_response(response)


@functools.cache
def create_query(where: str = None) -> ArcGISQuery:
    """creates a query class"""
    where = where or "1=1"

    service = ArcGISService(Config.SERVICE_URL)

    query = ArcGISQuery(service, where)

    return query


@functools.cache
def create_tileset_source() -> MapboxTilesetSource:
    """creates a mapbox instance with default settings"""
    return MapboxTilesetSource(user=Config.MAPBOX_USER, access_token=Config.MAPBOX_ACCESS_TOKEN)


@functools.cache
def create_tileset() -> MapboxTileset:
    """creates a mapbox tileset"""
    return MapboxTileset(name=Config.MAPBOX_TILESET_NAME, access_token=Config.MAPBOX_ACCESS_TOKEN)


# TODO apply to all functions that are using echo
def echo_json(data: t.Mapping):
    """utility for displaying data"""
    click.echo(json.dumps(data, indent=2))


@click.group
def cli():
    """click group"""


@cli.command
def info():
    """displays information about the data layer"""
    service = ArcGISService(Config.SERVICE_URL)
    echo_json(service.info)


@cli.command
@click.argument('where', nargs=-1)
def count(where: str = None):
    """displays the query count"""
    query = create_query(where)
    click.echo(query.count)

@cli.command
@click.argument('where', nargs=-1)
def extent(where: str = None):
    """displays the extent info"""
    query = create_query(where)
    click.echo(json.dumps(query.extent, indent=2))


@cli.command("tileset-list")
def tileset_list():
    """lists all the tilesets"""
    tileset_source = create_tileset_source()
    click.echo(json.dumps(tileset_source.list))


@cli.command
def download():
    """download data into a file"""
    query = create_query()

    with open(Config.OUTPUT_FILE, "x", encoding="utf-8") as fp:
        fp.writelines(query.feature_strings)


@cli.command
def upload():
    """uploads the contetns of the downloaded data to a tileset source"""
    tileset_source = create_tileset_source()

    with open(Config.OUTPUT_FILE, "r", encoding="utf-8") as fp:
        result = tileset_source.upload(Config.MAPBOX_ID, fp)

    click.echo(json.dumps(result))


def get_recipe() -> t.Mapping:
    """loads the recipe from the file"""
    with Config.RECIPE_MI_DNR_ROADS.open("r", encoding="utf-8") as fp:
        return json.load(fp)


@cli.command
def create():
    """creates a tileset based on the tileset source"""
    tileset = create_tileset()

    result = tileset.create(
        recipe=get_recipe(),
        description=Config.DESCRIPTION,
        attribution=Config.ATTRIBUTION,
        private=False,
    )

    click.echo(json.dumps(result, indent=2))

@cli.command("update-recipe")
def update_recipe():
    """updates the recipe"""
    tileset = create_tileset()
    result = tileset.update_recipe(get_recipe())
    click.echo(json.dumps(result, indent=2))


@cli.command
def jobs():
    """starts the job to publish the tileset"""
    tileset = create_tileset()
    result = tileset.jobs()
    click.echo(json.dumps(result, indent=2))


@cli.command
def publish():
    """starts the job to publish the tileset"""
    tileset = create_tileset()
    result = tileset.publish()
    click.echo(json.dumps(result, indent=2))


@cli.command("job-status")
@click.argument('job_id')
def job_status(job_id: str):
    tileset = create_tileset()
    result = tileset.job_status(job_id)
    click.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    cli()
