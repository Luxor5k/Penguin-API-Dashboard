from fastapi import APIRouter
from ..data.pymongo import db
from bson import json_util
from json import loads 

router = APIRouter()

#Da como resultado los pingüinos de una isla
@router.get("/island/{Island}")
def island(Island):
    project = {"Island": 1, "Individual ID": 1, "Sex": 1, "Species": 1, "_id":0}
    filter_ = {"Island" : Island}
    results = list(db["penguin"].find(filter_, project))
    if len(results) == 0:
        return {"error":"Island don't exist"}
    return loads(json_util.dumps(results))

#Buscamos un penguin en particular por su id
@router.get("/id/{Sample_Number}/{family}")
def get_data(Sample_Number, family=0):
    family = int(family)
    project = {"_id":0}
    filter_ = {"Sample Number": int(Sample_Number)}
    results = list(db["penguin"].find(filter_, project)[family:(family+1)])
    if len(results)==0:
        return {"error":"The ID don't exists"}
    return loads(json_util.dumps(results))

@router.get("/all")
def get_all():
    project = {"_id":0}
    results = list(db["penguin"].find({}, project))
    return loads(json_util.dumps(results))

@router.get("/species")
def species():
    project = {"Species":1, "_id":0}
    result = list(db["penguin"].find({},project).distinct("Species"))
    return loads(json_util.dumps(result))

@router.get("/islands")
def species():
    project = {"Island":1, "_id":0}
    result = list(db["penguin"].find({},project).distinct("Island"))
    return loads(json_util.dumps(result))

@router.get("/stats/{sample_number}/{family}")
def stats(sample_number, family=0):
    family = int(family)
    project = {"Culmen Length (mm)":1, "Culmen Depth (mm)":1, "Flipper Length (mm)":1, "Body Mass (g)":1, "_id":0}
    filter_ = {"Sample Number": int(sample_number)}
    results = list(db["penguin"].find(filter_, project)[family:(family+1)])
    return loads(json_util.dumps(results))


#Después de terminar streamlit si hay tiempo hacer una función para actualizar/agregar datos de penguins a la db