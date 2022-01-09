from fastapi import APIRouter
from ..data.pymongo import db
from bson import json_util
from json import loads 

router = APIRouter()

#AVG de Bodymass
@router.get("/avg/island/bdmass")
def avg_island_bdmass():
    pipeline = [
        {"$match":{"body_mass_g":{"$ne":None,"$type":"int"}}},
        {"$group":{'_id':"$island", "avg": {'$avg':"$body_mass_g"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))

#AVG de Flipper length
@router.get("/avg/island/fliplength")
def avg_island_bdmass():
    pipeline = [
        {"$match":{"flipper_length_mm":{"$ne":None, "$type":"int"}}},
        {"$group":{'_id':"$island", "avg": {'$avg':"$flipper_length_mm"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))

#AVG culmen_depth_mm
@router.get("/avg/island/culmendepth")
def avg_island_culmendepth():
    pipeline = [
        {"$match":{"culmen_depth_mm":{"$ne":None, "$type":"int"}}},
        {"$group":{'_id':"$island", "avg": {'$avg':"$culmen_depth_mm"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))

#AVG culmen_length_mm
@router.get("/avg/island/culmenlength")
def avg_island_bdmass():
    pipeline = [
        {"$match":{"culmen_length_mm":{"$ne":None,"$type":"int"}}},
        {"$group":{'_id':"$island", "avg": {'$avg':"$culmen_length_mm"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))

@router.get("/avg/island/all")
def avg_island_all():
    pipeline = [
        {"$match":{"culmen_length_mm":{"$ne":None,"$type":"int"}, "culmen_depth_mm":{"$ne":None,"$type":"int"}, "flipper_length_mm":{"$ne":None, "$type":"int"}, "body_mass_g":{"$ne":None,"$type":"int"}}},
        {"$group":{'_id':"$island", "culmen_length": {'$avg':"$culmen_length_mm"}, "culmendepth":{'$avg':"$culmen_depth_mm"}, "flipperlength": {'$avg':"$flipper_length_mm"}, "bodymass": {'$avg':"$body_mass_g"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))


@router.get("/avg/island/dream")
def avg_island_all():
    pipeline = [
        {"$match":{"culmen_length_mm":{"$ne":None,"$type":"int"}, "culmen_depth_mm":{"$ne":None,"$type":"int"}, "flipper_length_mm":{"$ne":None, "$type":"int"}, "body_mass_g":{"$ne":None,"$type":"int"}}},
        {"$group":{'_id':"$island", "culmen_length": {'$avg':"$culmen_length_mm"}, "culmendepth":{'$avg':"$culmen_depth_mm"}, "flipperlength": {'$avg':"$flipper_length_mm"}, "bodymass": {'$avg':"$body_mass_g"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))
    
#AVG culmen_depth_mm
@router.get("/avg/{species}/culmendepth")
def avg_island_culmendepth(species):
    pipeline = [
        {"$match":{"culmen_depth_mm":{"$ne":None, "$type":"int"}}},
        {"$group":{"_id":f"{species}", "avg": {'$avg':"$culmen_depth_mm"}}},
        {"$sort":{"_id":1}}

    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))

