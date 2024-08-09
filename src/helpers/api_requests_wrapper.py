import json
import requests


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()
