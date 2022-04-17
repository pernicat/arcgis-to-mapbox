# arcgis_to_mapbox

## API Documentation

- [ArcGIS REST APIs Feature Service](https://developers.arcgis.com/rest/services-reference/enterprise/feature-service.htm)


## ArcGIS DNR_ROADS FeatureServer

https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services/DNR_ROADS/FeatureServer


Fields
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


## MI_DNR_ROADS_ORV_2022

## MI_DNR_ROADS_CLASS_2022

### Federal, State, Local Govt, Private, Other Road

Non-DNR Roads

### Secondary Forest Road

State Park campsite roads
State Park day-use roads
State Park service roads
2-track roads on state land

### Forest Access Route

2-track roads on state land

### Primary Forest Road 

State Park Main Roads

### Administration Access Only

None

## MI_DNR_ROADS_