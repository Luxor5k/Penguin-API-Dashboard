from config.api import url
import requests

def get_for_id(id):
    return requests.get(url+f"/id/{id}").json()
