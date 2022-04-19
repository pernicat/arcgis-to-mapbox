"""cli tool definitions"""
import functools
import json
import typing as t

import click

from config import Config
from .arcgis import ArcGISService, ArcGISQuery
from .mapbox import MapboxTileset, MapboxTilesetSource


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
    echo_json(query.extent)



@cli.command("tileset-list")
def tileset_list():
    """lists all the tilesets"""
    tileset_source = create_tileset_source()
    echo_json(tileset_source.list)


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
