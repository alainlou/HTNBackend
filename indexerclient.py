import requests
import urllib.parse
import json

BASE_URL = 'https://api.videoindexer.ai'
ACCOUNT_ID = ''
OCP_KEY = ''
LOCATION = '/trial'

class IndexerClient:
  def __init__(self):
    self.token = '**NOT INITIALIZED**'
    print("Indexer Client started")

  def getAccessToken(self):
    uri = BASE_URL + '/auth/trial/Accounts/' + ACCOUNT_ID + '/AccessToken'
    headers = {
      'Ocp-Apim-Subscription-Key': OCP_KEY,
    }
    r = requests.get(uri, headers=headers)
    self.token = r.json()

  def requestByIndex(self, videoId):
    params = {
      'name': 'video.mp4',
      'privacy': 'Private',
      'language': 'English',
      'accessToken': self.token,
    }
    location = '/trial'
    uri = BASE_URL + location + '/Accounts/' + ACCOUNT_ID + '/Videos/' + videoId + '/Index?' + urllib.parse.urlencode(params)
    r = requests.get(uri).json()
    return r

  def listVideos(self):
    params = {
        'accessToken': self.token
    }
    uri = BASE_URL + LOCATION + '/Accounts/' + ACCOUNT_ID + '/Videos?' + urllib.parse.urlencode(params)
    r = requests.get(uri).json()
    return r

  def getDownloadURL(self, videoId):      
    uri = BASE_URL + LOCATION + '/Accounts/' + ACCOUNT_ID + '/Videos/' + videoId + '/Index?' + urllib.parse.urlencode()   
    r = requests.get(uri).json()
    return r

  def testReturn(self, word):
    return word
# indexer = IndexerClient()
# indexer.getAccessToken()
# indexer.requestByIndex('198c26215e')
