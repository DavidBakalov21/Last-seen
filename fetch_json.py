import requests


def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()
    return json_data

