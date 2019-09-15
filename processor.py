#concat indexerclient and database client
from indexerclient import IndexerClient
import json

# VIDEOID = '198c26215e'

class Processor:
  def __init__(self):
    self.indexerClient = IndexerClient()
    self.indexerClient.getAccessToken()

  def clean(self):
    vids = self.indexerClient.listVideos()['results']
    ids = []
    for i in range(len(vids)):
      ids.append(vids[i]['id'])
    response = {
      'data': []
    }
    for id in ids:
      result = self.indexerClient.requestByIndex(id)
      r = result['summarizedInsights']['keywords']
      response['data'].append(r)
    return response

  def getVideoURL(self):
    vids = self.indexerClient.listVideos()['results']
    ids = []
    for vid in vids:
      ids.append(vid['id'])
    return self.indexerClient.getDownloadURL(ids[0])
  
  def getVideoById(self, videoId):
    return self.indexerClient.requestByIndex(videoId)

  def test(self):
    return self.indexerClient.listVideos()

  def organizeByKeywords(self, jsonThing):
    #JSON
    #return('gets up to here')
    keywords = jsonThing['summarizedInsights']
    return keywords
    