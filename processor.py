#concat indexerclient and database client
from indexerclient import IndexerClient

VIDEOID = '198c26215e'

class Processor:
  def __init__(self):
    self.indexerClient = IndexerClient()
    self.indexerClient.getAccessToken()
    print(self.indexerClient.requestByIndex(VIDEOID))
  
  def getVideo(self):
    self.indexerClient.requestByIndex(VIDEOID)


  
    # def search(phrase):
    #     return indexerClient.search(phrase)