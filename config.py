"""loads dotenv and creates the configuration class"""
import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()


class Config:  # pylint: disable=too-few-public-methods
    """configuration"""
    ROOT_DIR = Path(__file__).parent

    MI_DNR_ROADS_URL = (
        "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS"
        "/rest/services/DNR_ROADS/FeatureServer"
    )
    MI_DNR_OPEN_TRAILS_URL = (
        "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS"
        "/rest/services/open_Trails/FeatureServer"
    )

    MAPBOX_USER = "pernicat"

    # https://account.mapbox.com/access-tokens
    # scopes: TILESET:LIST, TILESET:READ, TILESET:WRITE, DATASETS:READ, DATASETS:LIST
    MAPBOX_ACCESS_TOKEN = os.environ.get("MAPBOX_ACCESS_TOKEN")
