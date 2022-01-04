from config.api import url
import requests

def get_for_id(id, family):
    return requests.get(url+f"/id/{id}/{family}").json()

def get_stats(id, family):
    return requests.get(url+f"/stats/{id}/{family}").json()

def get_avg_bdmass():
    return requests.get(url+f"/avg/island/bdmass").json()