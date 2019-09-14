import requests
import urllib.parse
import json

BASE_URL = 'https://api.videoindexer.ai'
USER_ID = ''
SUB_KEY = ''

params = urllib.parse.urlencode({
    'name': 'video.mp4',
    'privacy': 'Private',
    'language': 'English',
})

class IndexerClient:
    def __init__(self):
        print("Indexer Client started")

    def getAccessToken(self):
        uri = BASE_URL + '/auth/trial/Accounts/' + USER_ID + '/AccessToken'
        headers = {
            'Ocp-Apim-Subscription-Key': SUB_KEY,
        }
        r = requests.get(uri, headers=headers)
        print(r.json())

    def search(phrase):
        uri = BASE_URL + '/Breakdowns/Api/Partner/Breakdowns?'
        # r = requests.post(url, params=params, files=form_data, headers=headers)
        # print(r.url)
        # print(json.dumps(r.json(), indent=2))

