import requests
import urllib.parse
import json

BASE_URL = 'https://api.videoindexer.ai'
USER_ID = ''
SUB_KEY = ''


class IndexerClient:
  def __init__(self):
    self.params = {
      'name': 'video.mp4',
      'privacy': 'Private',
      'language': 'English',
      'accessToken': '',
    }
    print("Indexer Client started")

  def getAccessToken(self):
    uri = BASE_URL + '/auth/trial/Accounts/' + ACCOUNT_ID + '/AccessToken'
    headers = {
      'Ocp-Apim-Subscription-Key': OCP_KEY,
    }
    r = requests.get(uri, headers=headers)
    # return r.json()
    print('Access Token: ')
    # print(r.json())
    self.params['accessToken'] = r.json()
    # params = urllib.parse.urlencode(params)

  def requestByIndex(self, videoId):
    location = '/trial'
    uri = BASE_URL + location + '/Accounts/' + ACCOUNT_ID + '/Videos/' + videoId + 'Index' + urllib.parse.urlencode(self.params) #\
          # + self.getAccessToken()
    print(uri)
    # r = requests.get(uri)
    # def search(phrase):
    #     uri = BASE_URL + '/Breakdowns/Api/Partner/Breakdowns?'
        # r = requests.post(url, params=params, files=form_data, headers=headers)
        # print(r.url)
        # print(json.dumps(r.json(), indent=2))
indexer = IndexerClient()
indexer.getAccessToken()
indexer.requestByIndex('198c26215e')
