"""cli tool definitions"""
import functools
import json
import typing as t

import click
import yaml

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
def create_tileset(name: str) -> MapboxTileset:
    """creates a mapbox tileset"""
    return MapboxTileset(name=name, access_token=Config.MAPBOX_ACCESS_TOKEN)


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


def tileset_source_command(func: t.Callable[[MapboxTilesetSource, ...], t.Any]) -> callable:
    """wraps commands to inject a tileset source"""
    @cli.command(func.__name__)
    def wrapper(**kwargs):
        return func(tileset_source=create_tileset_source(), **kwargs)

    return wrapper


@click.argument("mapbox_id", type=str)
@click.argument("filename", type=click.Path(exists=False))
@tileset_source_command
def upload(tileset_source: MapboxTilesetSource, mapbox_id: str, filename: str):
    """uploads the contetns of the downloaded data to a tileset source"""
    tileset_source = create_tileset_source()

    with open(filename, "r", encoding="utf-8") as fp:
        result = tileset_source.upload(mapbox_id, fp)

    echo_json(result)


def get_json(filename) -> t.Mapping:
    """loads json from a file"""
    with open(filename, "r", encoding="utf-8") as fp:
        return json.load(fp)
    

def get_yaml(filename) -> t.Mapping:
    """loads yaml from a file"""
    with open(filename, "r", encoding="utf-8") as fp:
        return yaml.safe_load(fp)


def tileset_command(func: t.Callable[[MapboxTileset, ...], t.Any]) -> callable:
    """wraps commands to inject a tileset"""
    @cli.command(func.__name__.replace("_", "-"))
    @click.argument("tileset", type=str)
    def wrapper(tileset: str, **kwargs):
        return func(tileset=create_tileset(tileset), **kwargs)

    return wrapper


@click.argument("tileset_file", type=click.Path(exists=True))
@tileset_command
def create(tileset: MapboxTileset, tileset_file: str):
    """creates a tileset based on the tileset source"""
    data = get_yaml(tileset_file)
    result = tileset.create(**data)
    echo_json(result)


@click.argument("tileset_file", type=click.Path(exists=True))
@tileset_command
def update_recipe(tileset: MapboxTileset, tileset_file: str):
    """updates the recipe"""
    data = get_yaml(tileset_file)
    result = tileset.update_recipe(data['recipe'])
    echo_json(result)


@tileset_command
def jobs(tileset: MapboxTileset):
    """displays the job to publish the tileset"""
    result = tileset.jobs()
    echo_json(result)


@tileset_command
def publish(tileset: MapboxTileset):
    """starts the job to publish the tileset"""
    result = tileset.publish()
    echo_json(result)


@click.argument('job_id')
@tileset_command
def job_status(tileset: MapboxTileset, job_id: str):
    """gets the status of a specific job"""
    result = tileset.job_status(job_id)
    echo_json(result)
