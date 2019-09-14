#concat indexerclient and database client
from indexerclient import IndexerClient
import json

# VIDEOID = '198c26215e'

class Processor:
  def __init__(self):
    self.indexerClient = IndexerClient()
    self.indexerClient.getAccessToken()
  
  def getVideoById(self, videoId):
    return self.indexerClient.requestByIndex(videoId)

  def organizeByKeywords(self, jsonThing):
    #JSON
    #return('gets up to here')
    keywords = jsonThing['summarizedInsights']
    return keywords
    