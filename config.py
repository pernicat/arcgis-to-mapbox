"""loads dotenv and creates the configuration class"""
import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()


class Config:
    """configuration"""
    ROOT_DIR = Path(__file__).parent

    HOST = "services3.arcgis.com"
    CONTEXT = "Jdnp1TjADvSDxMAX/ArcGIS"
    SERVICE_NAME = "DNR_ROADS"
    SERVICE_TYPE = "FeatureServer"
    SERVICE_LAYER = 0
    OPERATION = "query"
    SERVICE_URL = f"https://{HOST}/{CONTEXT}/rest/services/{SERVICE_NAME}/{SERVICE_TYPE}"
    QUERY_URL = f"{SERVICE_URL}/{SERVICE_LAYER}/{OPERATION}"

    MI_DNR_ROADS = "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services/DNR_ROADS/FeatureServer"
    MI_DNR_OPEN_TRAILS_URL = "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services/open_Trails/FeatureServer"

    ARCGIS_SERVICE_URLS ={
        "MI_DNR_ROADS": MI_DNR_ROADS,
        "MI_DNR_OPEN_TRAILS": MI_DNR_OPEN_TRAILS_URL
    }

    MAPBOX_USER = "pernicat"
    MAPBOX_ID = "MI_DNR_ROADS_2022"
    # https://account.mapbox.com/access-tokens
    # scopes: TILESET:LIST, TILESET:READ, TILESET:WRITE, DATASETS:READ, DATASETS:LIST
    MAPBOX_ACCESS_TOKEN = os.environ.get("MAPBOX_ACCESS_TOKEN")

    RECIPE_MI_DNR_ROADS = ROOT_DIR / "recipes" / "mi_dnr_roads_2022.json"
    ATTRIBUTION = [
        {
            "text": "Michigan DNR 2022",
            "link": "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services/DNR_ROADS/FeatureServer"
        }
    ]

    DESCRIPTION = "Michigan DNR roads 2022"

    MAPBOX_TILESET_NAME = f"{MAPBOX_USER}.{MAPBOX_ID}"

    OUTPUT_FILE = "arcgis.jsonl"
