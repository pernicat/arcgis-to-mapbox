YEAR := $(shell date '+%Y')

gis_download = python -m gistools download --service=MI_DNR_OPEN_TRAILS --layer=${1} ${2}
gis_upload = python -m gistools upload ${1} ${2} > ${3}

.PHONY: all downloads uploads templates tilesets publish
.DELETE_ON_ERROR:

all: downloads uploads templates tilesets publish

downloads: \
	var/mi_dnr_roads_$(YEAR).jsonl \
	var/mi_dnr_water_trails_$(YEAR).jsonl \
	var/mi_dnr_hiking_trails_$(YEAR).jsonl \
	var/mi_dnr_bicycle_trails_$(YEAR).jsonl \
	var/mi_dnr_equestrian_trails_$(YEAR).jsonl \
	var/mi_dnr_ski_trails_$(YEAR).jsonl \
	var/mi_dnr_snowshoe_trails_$(YEAR).jsonl \
	var/mi_dnr_motorcycle_trails_$(YEAR).jsonl \
	var/mi_dnr_atv_trails_$(YEAR).jsonl \
	var/mi_dnr_orv_routes_$(YEAR).jsonl \
	var/mi_dnr_snowmobile_trails_$(YEAR).jsonl \
	var/mi_dnr_mccct_$(YEAR).jsonl \
	var/mi_dnr_railtrails_$(YEAR).jsonl \
	var/mi_dnr_hunter_walking_trails_$(YEAR).jsonl \
	var/mi_dnr_trails_$(YEAR).jsonl \
	var/mi_dnr_iron_belle_trail_$(YEAR).jsonl \
	var/mi_dnr_trail_groom_sponser_$(YEAR).jsonl \
	var/mi_dnr_recreation_grant_points_$(YEAR).jsonl \
	var/mi_dnr_recreation_grant_polys_$(YEAR).jsonl \
	var/mi_dnr_recreation_grant_coordinator_regions_$(YEAR).jsonl \
	var/mi_dnr_map_extends_$(YEAR).jsonl \
	var/mi_dnr_nonmotorized_trails_$(YEAR).jsonl \
	var/mi_dnr_trail_region_boundries_$(YEAR).jsonl \

var/mi_dnr_roads_$(YEAR).jsonl:
	python -m gistools download ${@}
var/mi_dnr_water_trails_$(YEAR).jsonl:
	$(call gis_download,0,${@})
var/mi_dnr_hiking_trails_$(YEAR).jsonl:
	$(call gis_download,1,${@})
var/mi_dnr_bicycle_trails_$(YEAR).jsonl:
	$(call gis_download,2,${@})
var/mi_dnr_equestrian_trails_$(YEAR).jsonl:
	$(call gis_download,3,${@})
var/mi_dnr_ski_trails_$(YEAR).jsonl:
	$(call gis_download,4,${@})
var/mi_dnr_snowshoe_trails_$(YEAR).jsonl:
	$(call gis_download,5,${@})
var/mi_dnr_motorcycle_trails_$(YEAR).jsonl:
	$(call gis_download,6,${@})
var/mi_dnr_atv_trails_$(YEAR).jsonl:
	$(call gis_download,7,${@})
var/mi_dnr_orv_routes_$(YEAR).jsonl:
	$(call gis_download,8,${@})
var/mi_dnr_snowmobile_trails_$(YEAR).jsonl:
	$(call gis_download,9,${@})
var/mi_dnr_mccct_$(YEAR).jsonl:
	$(call gis_download,10,${@})
var/mi_dnr_railtrails_$(YEAR).jsonl:
	$(call gis_download,11,${@})
var/mi_dnr_hunter_walking_trails_$(YEAR).jsonl:
	$(call gis_download,12,${@})
var/mi_dnr_trails_$(YEAR).jsonl:
	$(call gis_download,13,${@})
var/mi_dnr_iron_belle_trail_$(YEAR).jsonl:
	$(call gis_download,14,${@})
var/mi_dnr_trail_groom_sponser_$(YEAR).jsonl:
	$(call gis_download,15,${@})
var/mi_dnr_recreation_grant_points_$(YEAR).jsonl:
	$(call gis_download,16,${@})
var/mi_dnr_recreation_grant_polys_$(YEAR).jsonl:
	$(call gis_download,17,${@})
var/mi_dnr_recreation_grant_coordinator_regions_$(YEAR).jsonl:
	$(call gis_download,18,${@})
var/mi_dnr_map_extends_$(YEAR).jsonl:
	$(call gis_download,19,${@})
var/mi_dnr_nonmotorized_trails_$(YEAR).jsonl:
	$(call gis_download,20,${@})
var/mi_dnr_trail_region_boundries_$(YEAR).jsonl:
	$(call gis_download,21,${@})

uploads: \
	var/mi_dnr_roads_$(YEAR)-upload.json \
	var/mi_dnr_water_trails_$(YEAR)-upload.json \
	var/mi_dnr_hiking_trails_$(YEAR)-upload.json \
	var/mi_dnr_bicycle_trails_$(YEAR)-upload.json \
	var/mi_dnr_equestrian_trails_$(YEAR)-upload.json \
	var/mi_dnr_ski_trails_$(YEAR)-upload.json \
	var/mi_dnr_snowshoe_trails_$(YEAR)-upload.json \
	var/mi_dnr_motorcycle_trails_$(YEAR)-upload.json \
	var/mi_dnr_atv_trails_$(YEAR)-upload.json \
	var/mi_dnr_orv_routes_$(YEAR)-upload.json \
	var/mi_dnr_snowmobile_trails_$(YEAR)-upload.json \
	var/mi_dnr_mccct_$(YEAR)-upload.json \
	var/mi_dnr_railtrails_$(YEAR)-upload.json \
	var/mi_dnr_hunter_walking_trails_$(YEAR)-upload.json \
	var/mi_dnr_trails_$(YEAR)-upload.json \
	var/mi_dnr_iron_belle_trail_$(YEAR)-upload.json \
	var/mi_dnr_trail_groom_sponser_$(YEAR)-upload.json \
	var/mi_dnr_recreation_grant_points_$(YEAR)-upload.json \
	var/mi_dnr_recreation_grant_polys_$(YEAR)-upload.json \
	var/mi_dnr_recreation_grant_coordinator_regions_$(YEAR)-upload.json \
	var/mi_dnr_map_extends_$(YEAR)-upload.json \
	var/mi_dnr_nonmotorized_trails_$(YEAR)-upload.json \
	var/mi_dnr_trail_region_boundries_$(YEAR)-upload.json

var/mi_dnr_roads_$(YEAR)-upload.json: var/mi_dnr_roads_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_ROADS_$(YEAR),$@)
var/mi_dnr_water_trails_$(YEAR)-upload.json: var/mi_dnr_water_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_WATER_TRAILS_$(YEAR),$@)
var/mi_dnr_hiking_trails_$(YEAR)-upload.json: var/mi_dnr_hiking_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_HIKING_TRAILS_$(YEAR),$@)
var/mi_dnr_bicycle_trails_$(YEAR)-upload.json: var/mi_dnr_bicycle_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_BICYCLE_TRAILS_$(YEAR),$@)
var/mi_dnr_equestrian_trails_$(YEAR)-upload.json: var/mi_dnr_equestrian_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_EQUESTRIAN_TRAILS_$(YEAR),$@)
var/mi_dnr_ski_trails_$(YEAR)-upload.json: var/mi_dnr_ski_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_SKI_TRAILS_$(YEAR),$@)
var/mi_dnr_snowshoe_trails_$(YEAR)-upload.json: var/mi_dnr_snowshoe_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_SHOWSHOE_TRAILS_$(YEAR),$@)
var/mi_dnr_motorcycle_trails_$(YEAR)-upload.json: var/mi_dnr_motorcycle_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_MOTORCYCLE_TRAILS_$(YEAR),$@)
var/mi_dnr_atv_trails_$(YEAR)-upload.json: var/mi_dnr_atv_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_ATV_TRAILS_$(YEAR),$@)
var/mi_dnr_orv_routes_$(YEAR)-upload.json: var/mi_dnr_orv_routes_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_ORV_ROUTES_$(YEAR),$@)
var/mi_dnr_snowmobile_trails_$(YEAR)-upload.json: var/mi_dnr_snowmobile_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_SNOWMOBILE_TRAILS_$(YEAR),$@)
var/mi_dnr_mccct_$(YEAR)-upload.json: var/mi_dnr_mccct_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_MCCCT_TRAILS_$(YEAR),$@)
var/mi_dnr_railtrails_$(YEAR)-upload.json: var/mi_dnr_railtrails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_RAILTRAILS_TRAILS_$(YEAR),$@)
var/mi_dnr_hunter_walking_trails_$(YEAR)-upload.json: var/mi_dnr_hunter_walking_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_HUNTER_TRAILS_$(YEAR),$@)
var/mi_dnr_trails_$(YEAR)-upload.json: var/mi_dnr_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_TRAILS_$(YEAR),$@)
var/mi_dnr_iron_belle_trail_$(YEAR)-upload.json: var/mi_dnr_iron_belle_trail_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_IRON_BELLE_TRAILS_$(YEAR),$@)
var/mi_dnr_trail_groom_sponser_$(YEAR)-upload.json: var/mi_dnr_trail_groom_sponser_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_GROOM_SPONSER_TRAILS_$(YEAR),$@)
var/mi_dnr_recreation_grant_points_$(YEAR)-upload.json: var/mi_dnr_recreation_grant_points_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_REC_GRANT_POINTS_$(YEAR),$@)
var/mi_dnr_recreation_grant_polys_$(YEAR)-upload.json: var/mi_dnr_recreation_grant_polys_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_REC_GRANT_POLYS_$(YEAR),$@)
var/mi_dnr_recreation_grant_coordinator_regions_$(YEAR)-upload.json: var/mi_dnr_recreation_grant_coordinator_regions_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_REC_GRANT_REGIONS_$(YEAR),$@)
var/mi_dnr_map_extends_$(YEAR)-upload.json: var/mi_dnr_map_extends_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_MAP_EXTENDS_TRAILS_$(YEAR),$@)
var/mi_dnr_nonmotorized_trails_$(YEAR)-upload.json: var/mi_dnr_nonmotorized_trails_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_NONMORORIZED_TRAILS_$(YEAR),$@)
var/mi_dnr_trail_region_boundries_$(YEAR)-upload.json: var/mi_dnr_trail_region_boundries_$(YEAR).jsonl
	$(call gis_upload,$<,MI_DNR_TRAIL_REGIONS_$(YEAR),$@)


templates: \
	tilesets/mi_dnr_open_trails_$(YEAR).yaml \
	tilesets/mi_dnr_roads_$(YEAR).yaml

tilesets/mi_dnr_roads_$(YEAR).yaml:
	YEAR=$(YEAR) envsubst < tilesets/mi_dnr_roads_TEMPLATE.yaml > ${@}
tilesets/mi_dnr_open_trails_$(YEAR).yaml:
	YEAR=$(YEAR) envsubst < tilesets/mi_dnr_open_trails_TEMPLATE.yaml > ${@}


tilesets: \
	var/MI_DNR_ROADS_$(YEAR)-create.json \
	var/MI_DNR_OPEN_TRIALS_$(YEAR)-create.json

var/MI_DNR_ROADS_$(YEAR)-create.json: tilesets/mi_dnr_roads_$(YEAR).yaml
	python -m gistools create MI_DNR_ROADS_$(YEAR) $< > $@
var/MI_DNR_OPEN_TRIALS_$(YEAR)-create.json: tilesets/mi_dnr_open_trails_$(YEAR).yaml
	python -m gistools create MI_DNR_OPEN_TRIALS_$(YEAR) $< > $@


publish: \
	var/MI_DNR_ROADS_$(YEAR)-publish.json \
	var/MI_DNR_OPEN_TRIALS_$(YEAR)-publish.json

var/MI_DNR_ROADS_$(YEAR)-publish.json: var/MI_DNR_ROADS_$(YEAR)-create.json
	python -m gistools publish MI_DNR_ROADS_$(YEAR) > ${@}
var/MI_DNR_OPEN_TRIALS_$(YEAR)-publish.json: var/MI_DNR_OPEN_TRIALS_$(YEAR)-create.json
	python -m gistools publish MI_DNR_OPEN_TRIALS_$(YEAR) > ${@}
