from config.api import url
import requests

def get_for_id(id, family):
    return requests.get(url+f"/id/{id}/{family}").json()

def get_stats(id, family):
    return requests.get(url+f"/stats/{id}/{family}").json()

def get_avg_bdmass():
    return requests.get(url+f"/avg/island/bdmass").json()

def get_avg_fliplength():
    return requests.get(url+f"/avg/island/fliplength").json()

def get_avg_culmendepth():
    return requests.get(url+f"/avg/island/culmendepth").json()

def get_avg_culmenlength():
    return requests.get(url+f"/avg/island/culmenlength").json()

def get_stats_species():
    return requests.get(url+f"/avg/all/culmendepth").json()

