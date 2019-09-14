import requests
import urllib.parse
import json

BASE_URL = 'https://api.videoindexer.ai'
API_KEY = ''

params = urllib.parse.urlencode({
    'name': 'video.mp4',
    'privacy': 'Private',
    'language': 'English',
})

headers = {
    'Ocp-Apim-Subscription-Key': '',
}

form_data = {}

class IndexerClient:
    def __init__(self):
        print("Indexer Client started")

    def search(phrase):
        url = BASE_URL + '/Breakdowns/Api/Partner/Breakdowns?'
        # r = requests.post(url, params=params, files=form_data, headers=headers)
        # print(r.url)
        # print(json.dumps(r.json(), indent=2))

