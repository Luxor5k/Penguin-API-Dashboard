from fastapi import APIRouter
from ..data.pymongo import db

router = APIRouter()

@router.get("/area/{Region}")
def area(Region):
    project = {"Region": 1, "Island": 1, "studyName": 1, "_id":0}
    filter_ = {"Region" : Region}
    results = db.find(filter_)
    return list(results)[:10]