# arcgis_to_mapbox

Tools for exporting data out of an ArcGIS Feature server and into a Mapbox data source



## Usage

```shell
poetry install
poetry shell
```

### Makefile

```shell
make all
```

### DNR Roads

```shell
export YEAR=$(date '+%Y')
python -m gistools download var/mi_dnr_roads_${YEAR}.jsonl
python -m gistools upload var/mi_dnr_roads_${YEAR}.jsonl MI_DNR_ROADS_${YEAR}
python -m gistools create MI_DNR_ROADS_${YEAR} tilesets/mi_dnr_roads_${YEAR}.yaml
python -m gistools publish MI_DNR_ROADS_${YEAR}
python -m gistools job-status MI_DNR_ROADS_${YEAR} clglfh3r4002h08l4ceyz61gh
```

### Other DNR Trails

download the shapefiles

```shell
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=0 var/mi_dnr_water_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=1 var/mi_dnr_hiking_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=2 var/mi_dnr_bicycle_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=3 var/mi_dnr_equestrian_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=4 var/mi_dnr_ski_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=5 var/mi_dnr_snowshoe_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=6 var/mi_dnr_motorcycle_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=7 var/mi_dnr_atv_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=8 var/mi_dnr_orv_routes_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=9 var/mi_dnr_snowmobile_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=10 var/mi_dnr_mccct_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=11 var/mi_dnr_railtrails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=12 var/mi_dnr_hunter_walking_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=13 var/mi_dnr_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=14 var/mi_dnr_iron_belle_trail_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=15 var/mi_dnr_trail_groom_sponser_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=16 var/mi_dnr_recreation_grant_points_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=17 var/mi_dnr_recreation_grant_polys_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=18 var/mi_dnr_recreation_grant_coordinator_regions_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=19 var/mi_dnr_map_extends_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=20 var/mi_dnr_nonmotorized_trails_${YEAR}.jsonl
python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=21 var/mi_dnr_trail_region_boundaries_${YEAR}.jsonl

```

Upload the shapefiles

```shell
python -m gistools upload var/mi_dnr_water_trails_${YEAR}.jsonl MI_DNR_WATER_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_hiking_trails_${YEAR}.jsonl MI_DNR_HIKING_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_bicycle_trails_${YEAR}.jsonl MI_DNR_BICYCLE_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_equestrian_trails_${YEAR}.jsonl MI_DNR_EQUESTRIAN_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_ski_trails_${YEAR}.jsonl MI_DNR_SKI_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_snowshoe_trails_${YEAR}.jsonl MI_DNR_SHOWSHOE_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_motorcycle_trails_${YEAR}.jsonl MI_DNR_MOTORCYCLE_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_atv_trails_${YEAR}.jsonl MI_DNR_ATV_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_orv_routes_${YEAR}.jsonl MI_DNR_ORV_ROUTES_${YEAR}
python -m gistools upload var/mi_dnr_snowmobile_trails_${YEAR}.jsonl MI_DNR_SNOWMOBILE_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_mccct_${YEAR}.jsonl MI_DNR_MCCCT_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_railtrails_${YEAR}.jsonl MI_DNR_RAILTRAILS_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_hunter_walking_trails_${YEAR}.jsonl MI_DNR_HUNTER_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_trails_${YEAR}.jsonl MI_DNR_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_iron_belle_trail_${YEAR}.jsonl MI_DNR_IRON_BELLE_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_trail_groom_sponser_${YEAR}.jsonl MI_DNR_GROOM_SPONSER_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_recreation_grant_points_${YEAR}.jsonl MI_DNR_REC_GRANT_POINTS_${YEAR}
python -m gistools upload var/mi_dnr_recreation_grant_polys_${YEAR}.jsonl MI_DNR_REC_GRANT_POLYS_${YEAR}
python -m gistools upload var/mi_dnr_recreation_grant_coordinator_regions_${YEAR}.jsonl MI_DNR_REC_GRANT_REGIONS_${YEAR}
python -m gistools upload var/mi_dnr_map_extends_${YEAR}.jsonl MI_DNR_MAP_EXTENDS_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_nonmotorized_trails_${YEAR}.jsonl MI_DNR_NONMORORIZED_TRAILS_${YEAR}
python -m gistools upload var/mi_dnr_trail_region_boundaries_${YEAR}.jsonl MI_DNR_TRAIL_REGIONS_${YEAR}
```

Create the the tileset

```shell
python -m gistools create MI_DNR_OPEN_TRIALS_${YEAR} tilesets/mi_dnr_open_trails_${YEAR}.yaml
```

Publish the tileset

```shell
python -m gistools publish MI_DNR_OPEN_TRIALS_${YEAR}
```

https://studio.mapbox.com/

Click `New style` -> `blank` 

`Layers` tab on the left column

By styles at the top click on `blank` and change the name of the style.


Click `+` 
Select `Custom Layer`
Under Source select the new tileset
Select the new tileset
Click the `Styles` tab
Click `</>` at the bottom
Copy and paste the style from `/styles`

To View: 11.77
44.708,-85.437

publish
share
Developer
Third Party
carto

Gaia GPS
Layers
Add Custom Source

## API Documentation

- [ArcGIS REST APIs Feature Service](https://developers.arcgis.com/rest/services-reference/enterprise/feature-service.htm)


## ArcGIS DNR_ROADS FeatureServer

https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services/DNR_ROADS/FeatureServer

### Field Specifications

```yaml
OBJECTID:
    type: int
    serial: true
ROADPRIMARY:
    alias: Road Primary Name
    type: string
SURFACETYPE:
    alias: Road Surface Type
    type: enum
    options:
        0: Paved
        1: Gravel
        2: Dirt and Native Material
        3: Highway
CONDITION:
    alias: Road Condition
    type: enum
    options:
        0: Failed
        1: Poor
        2: Fair
        3: Good
        4: Excellent
CLOSURECRITERIA:
    alias: Closure Criteria
    type: enum
    options:
        1: Closed - Environmental and resource protection
        2: Closed - Dedicated or nominated natural area
        3: Closed - Visual Quality objectives
        4: Closed - Proximity to private property
        5: Closed - Litter and dumping
        6: Closed - User safety
        7: Closed - Lack of legal access (easement needed)
        8: Closed - Road Density
        9: Closed - Reduce user conflict
        10: Closed - Poor road conditions
        11: (INACTIVE) Closed - Administrative Rule
        12: (INACTIVE) Closed - Land Use Order
        13: Closed - Deed Restriction
        14: Closed - Management Plan
        15: (INACTIVE) Closed - Temporary Management Access
        16: Closed - Military Land Restrictions
        17: Closed - Grouse Enhancement Management
        20: Needs Review
        50: Not a DNR Road - See local government laws
        100: Open
        101: Open - Economic Impact
        102: Open - User Access
        103: Open - Connectivity
OWNER:
    alias: Road Owner
    type: enum
    options:
        0: Unspecified
        1: State
        2: Federal
        3: County
        4: Private
        5: Undesignated
ROADOPENINGDATE:
    alias: Road Opening Date
    type: date
ROADCLOSINGDATE:
    alias: Road Closing Date
    type: date
ORVSTATUS:
    alias: ORV Status
    type: enum
    options: @CLOSURECRITERIA.options
ORVOPENINGDATE:
    alias: ORV Opening Date
    type: date
ORVCLOSINGDATE:
    alias: ORV Closing Date
    type: date
LENGTH:
    alias: Length (Miles)
    type: float
ROADTYPE:
    alias: Road Class
    type: enum
    options:
        0: Primary Forest Road
        1: Secondary Forest Road
        3: Administrative Access Only
        4: Federal, State, Local Govt, Private, Other Road
        2: Forest Access Route
RoadORVUse:
    alias: Road ORV Use
    type: string
    options:
        - DNR Roads Closed to ORV's
        - Military Roads Closed to ORV's
        - DNR Roads Open to ORV's
        - Military Roads Open to ORV's
        - Seasonal DNR Roads Seasonal Closures to ORV's
        - Military Roads Seasonally Closed to ORVs
        - Non-DNR Roads
GlobalID:
    type: uuid
Shape__Length:
    type: float

```

## ArcGIS open_trails FeatureServer - ORV Routes



### Raw Field Specification
```yaml
[
    {
        "name" : "OBJECTID", 
        "type" : "esriFieldTypeOID", 
        "alias" : "OBJECTID", 
        "sqlType" : "sqlTypeOther", 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Unique_ID", 
        "type" : "esriFieldTypeString", 
        "alias" : "Unique_ID", 
        "sqlType" : "sqlTypeOther", 
        "length" : 20, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Link_ID", 
        "type" : "esriFieldTypeString", 
        "alias" : "Link_ID", 
        "sqlType" : "sqlTypeOther", 
        "length" : 20, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "PRD_DB", 
        "type" : "esriFieldTypeString", 
        "alias" : "PRD_DB", 
        "sqlType" : "sqlTypeOther", 
        "length" : 50, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "PRD_Join", 
        "type" : "esriFieldTypeInteger", 
        "alias" : "PRD_Join", 
        "sqlType" : "sqlTypeOther", 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "State_Designated_Trail", 
        "type" : "esriFieldTypeString", 
        "alias" : "State_Designated_Trail", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Approval_Status", 
        "type" : "esriFieldTypeString", 
        "alias" : "Approval_Status", 
        "sqlType" : "sqlTypeOther", 
        "length" : 20, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Use_Category", 
        "type" : "esriFieldTypeString", 
        "alias" : "Use_Category", 
        "sqlType" : "sqlTypeOther", 
        "length" : 13, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Status", 
        "type" : "esriFieldTypeString", 
        "alias" : "Status", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Edit_Type", 
        "type" : "esriFieldTypeString", 
        "alias" : "Edit_Type", 
        "sqlType" : "sqlTypeOther", 
        "length" : 16, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Collection_Type", 
        "type" : "esriFieldTypeString", 
        "alias" : "Collection_Type", 
        "sqlType" : "sqlTypeOther", 
        "length" : 18, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Collection_Source", 
        "type" : "esriFieldTypeString", 
        "alias" : "Collection_Source", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Collection_Date", 
        "type" : "esriFieldTypeDate", 
        "alias" : "Collection_Date", 
        "sqlType" : "sqlTypeOther", 
        "length" : 8, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "QAQC_Status", 
        "type" : "esriFieldTypeString", 
        "alias" : "QAQC_Status", 
        "sqlType" : "sqlTypeOther", 
        "length" : 32, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "QAQC_Approved_By", 
        "type" : "esriFieldTypeString", 
        "alias" : "QAQC_Approved_By", 
        "sqlType" : "sqlTypeOther", 
        "length" : 100, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "QAQC_Date", 
        "type" : "esriFieldTypeDate", 
        "alias" : "QAQC_Date", 
        "sqlType" : "sqlTypeOther", 
        "length" : 8, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Edit_Date", 
        "type" : "esriFieldTypeDate", 
        "alias" : "Edit_Date", 
        "sqlType" : "sqlTypeOther", 
        "length" : 8, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Edit_Name", 
        "type" : "esriFieldTypeString", 
        "alias" : "Edit_Name", 
        "sqlType" : "sqlTypeOther", 
        "length" : 50, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Comments", 
        "type" : "esriFieldTypeString", 
        "alias" : "Comments", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "ORV_Route", 
        "type" : "esriFieldTypeString", 
        "alias" : "ORV_Route", 
        "sqlType" : "sqlTypeOther", 
        "length" : 20, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "ORV_Route_Name", 
        "type" : "esriFieldTypeString", 
        "alias" : "ORV_Route_Name", 
        "sqlType" : "sqlTypeOther", 
        "length" : 255, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "ORV_Restricted_Route", 
        "type" : "esriFieldTypeString", 
        "alias" : "ORV_Restricted_Route", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "License_Type", 
        "type" : "esriFieldTypeString", 
        "alias" : "License_Type", 
        "sqlType" : "sqlTypeOther", 
        "length" : 26, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Trail_Network", 
        "type" : "esriFieldTypeString", 
        "alias" : "Trail_Network", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Owner", 
        "type" : "esriFieldTypeString", 
        "alias" : "Owner", 
        "sqlType" : "sqlTypeOther", 
        "length" : 125, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Administrator", 
        "type" : "esriFieldTypeString", 
        "alias" : "Administrator", 
        "sqlType" : "sqlTypeOther", 
        "length" : 50, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Width", 
        "type" : "esriFieldTypeString", 
        "alias" : "Width", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Surface", 
        "type" : "esriFieldTypeString", 
        "alias" : "Surface", 
        "sqlType" : "sqlTypeOther", 
        "length" : 51, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Seasonal_Restriction", 
        "type" : "esriFieldTypeString", 
        "alias" : "Seasonal_Restriction", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Seasonal_Restriction_Comment", 
        "type" : "esriFieldTypeString", 
        "alias" : "Seasonal_Restriction_Comment", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Special_Designation", 
        "type" : "esriFieldTypeString", 
        "alias" : "Special_Designation", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Special_Designation_Comment", 
        "type" : "esriFieldTypeString", 
        "alias" : "Special_Designation_Comment", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "On_Road", 
        "type" : "esriFieldTypeString", 
        "alias" : "On_Road", 
        "sqlType" : "sqlTypeOther", 
        "length" : 11, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "ROW", 
        "type" : "esriFieldTypeString", 
        "alias" : "ROW", 
        "sqlType" : "sqlTypeOther", 
        "length" : 18, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "ROW_Comments", 
        "type" : "esriFieldTypeString", 
        "alias" : "ROW_Comments", 
        "sqlType" : "sqlTypeOther", 
        "length" : 400, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Miles", 
        "type" : "esriFieldTypeDouble", 
        "alias" : "Miles", 
        "sqlType" : "sqlTypeOther", 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Groom_Sponsor", 
        "type" : "esriFieldTypeString", 
        "alias" : "Groom_Sponsor", 
        "sqlType" : "sqlTypeOther", 
        "length" : 100, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "CreationDate", 
        "type" : "esriFieldTypeDate", 
        "alias" : "CreationDate", 
        "sqlType" : "sqlTypeOther", 
        "length" : 8, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Creator", 
        "type" : "esriFieldTypeString", 
        "alias" : "Creator", 
        "sqlType" : "sqlTypeOther", 
        "length" : 128, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "EditDate", 
        "type" : "esriFieldTypeDate", 
        "alias" : "EditDate", 
        "sqlType" : "sqlTypeOther", 
        "length" : 8, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Editor", 
        "type" : "esriFieldTypeString", 
        "alias" : "Editor", 
        "sqlType" : "sqlTypeOther", 
        "length" : 128, 
        "domain" : null, 
        "defaultValue" : null
    }, 
    {
        "name" : "Shape__Length", 
        "type" : "esriFieldTypeDouble", 
        "alias" : "Shape__Length", 
        "sqlType" : "sqlTypeDouble", 
        "domain" : null, 
        "defaultValue" : null
    }
]
```

## License
This project is free for personal and educational use only.

Commercial use (including use by for-profit companies or as part of paid services or products) requires written permission from the author.

If you're interested in using this commercially, please contact me.
