# arcgis_to_mapbox

Tools for exporting data out of an ArcGIS Feature server and into a Mapbox data source

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
