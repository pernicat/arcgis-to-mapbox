"""cli tool definitions"""
import functools
import json
import typing as t

import click

from config import Config
from .arcgis import ArcGISService, ArcGISQuery
from .mapbox import MapboxTileset, MapboxTilesetSource

SERVICES = {
    "MI_DNR_ROADS": Config.MI_DNR_ROADS_URL,
    "MI_DNR_OPEN_TRAILS": Config.MI_DNR_OPEN_TRAILS_URL,
}

@functools.cache
def create_query(service_name: str, layer=0, where: str = None) -> ArcGISQuery:
    """creates a query class"""

    where = where or "1=1"

    service = ArcGISService(SERVICES[service_name.upper()], layer)

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


def query_command(func: t.Callable[[ArcGISQuery, ...], t.Any]) -> callable:
    """decorator for wrapping a cli command with query options"""
    @cli.command(func.__name__)
    @click.option(
        "--service",
        default="MI_DNR_ROADS",
        type=click.Choice(SERVICES.keys(), case_sensitive=False)
    )
    @click.option("--layer", default=0, type=int)
    @click.option("--where", default=None)
    def wrapper(service: str, layer: int, where: str = None, **kwargs):
        query = create_query(service, layer, where)
        return func(query=query, **kwargs)

    return wrapper

@query_command
def count(query: ArcGISQuery):
    """displays the query count"""
    click.echo(query.count)


@query_command
def extent(query: ArcGISQuery):
    """displays the extent info"""
    echo_json(query.extent)



@cli.command("tileset-list")
def tileset_list():
    """lists all the tilesets"""
    tileset_source = create_tileset_source()
    echo_json(tileset_source.list)



@click.argument("filename", type=click.Path(exists=False))
@query_command
def download(query:ArcGISQuery, filename: str):
    """download data into a file"""
    with open(filename, "x", encoding="utf-8") as fp:
        fp.writelines(query.feature_strings)


@cli.command
def upload():
    """uploads the contetns of the downloaded data to a tileset source"""
    tileset_source = create_tileset_source()

    with open(Config.OUTPUT_FILE, "r", encoding="utf-8") as fp:
        result = tileset_source.upload(Config.MAPBOX_ID, fp)

    echo_json(result)


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

    echo_json(result)

@cli.command("update-recipe")
def update_recipe():
    """updates the recipe"""
    tileset = create_tileset()
    result = tileset.update_recipe(get_recipe())
    echo_json(result)


@cli.command
def jobs():
    """starts the job to publish the tileset"""
    tileset = create_tileset()
    result = tileset.jobs()
    echo_json(result)


@cli.command
def publish():
    """starts the job to publish the tileset"""
    tileset = create_tileset()
    result = tileset.publish()
    echo_json(result)


@cli.command("job-status")
@click.argument('job_id')
def job_status(job_id: str):
    """gets the status of a specific job"""
    tileset = create_tileset()
    result = tileset.job_status(job_id)
    echo_json(result)
