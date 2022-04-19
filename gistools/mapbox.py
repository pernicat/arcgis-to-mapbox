"""MapBox classes"""
import logging
import typing as t

import requests

from .helpers import check_response

logger = logging.getLogger(__name__)


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
