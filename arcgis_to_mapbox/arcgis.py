"""ArcGIS classes"""
import functools
import json
import logging
import time
import typing as t

import requests

from arcgis_to_mapbox.exceptions import RequestError
from arcgis_to_mapbox.helpers import check_response

logger = logging.getLogger(__name__)

DEFAULT_WAITS = [1, 2, 5, 8, 15, 30, 600]


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
