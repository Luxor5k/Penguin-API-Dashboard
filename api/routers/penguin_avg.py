from fastapi import APIRouter
from ..data.pymongo import db
from bson import json_util
from json import loads 

router = APIRouter()

@router.get("/avg/island/bdmass")
def avg_culmen_length():
    pipeline = [
        {"$match":{"body_mass_g":{"$ne":None,"$type":"int"}}},
        {"$group":{'_id':"$island", "avg": {'$avg':"$body_mass_g"}}},
    ]
    results = list(db["penguin_size"].aggregate(pipeline))
    return loads(json_util.dumps(results))