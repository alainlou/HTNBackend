#concat indexerclient and database client
from indexerclient import IndexerClient
import json

TEST_VIDEO_ID = 'f11e461264'

class Processor:
  def __init__(self):
    self.indexerClient = IndexerClient()
    self.indexerClient.getAccessToken()

  def process(self, name):
    vids = self.indexerClient.listVideos()['results']
    ids = []
    for i in range(len(vids)):
      ids.append(vids[i]['id'])
    response = {
      'data': {
        'climate change': [],
        'mental health': [],
        'guns': [],
        'minimum wage': []
      }
    }
    # for id in ids:
    #   result = self.indexerClient.requestByIndex(id)
    #   key = result['summarizedInsights']['keywords']
    #   if(key)
    #   response['data'].append(r)
    # return response
    keys = self.indexerClient.requestByIndex(TEST_VIDEO_ID)['summarizedInsights']['keywords']
    return str(keys)
    for key in keys:
      if(key['name'] == 'climate change'):
        for obj in key['appearances']:
          response['data']['climate change'].append(obj['startTime'])
      elif(key['name'] == 'minimum wage'):
        for obj in key['appearances']:
          response['data']['minimum wage'].append(obj['startTime'])
      elif('gun' in key['name'] or key['name'] == 'assault weapon'):
        for obj in key['appearances']:
          response['data']['guns'].append(obj['startTime'])
      elif(key['name'] == 'mental health'):
        for obj in key['appearances']:
          response['data']['mental health'].append(obj['startTime'])
    return response

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

  def refresh(self):
    return self.indexerClient.getAccessToken()

  def test(self):
    return self.indexerClient.listVideos()

    
  def reformatJSON(self, jsonFile):
    # JSON
    # return('gets up to here')
    # Names of All Famous People in the Videos
    namedPeople = jsonFile['summarizedInsights']['namedPeople']
    # Topics contains "name" and "referenceId"
    # referenceId is the category "name" belongs in (i.e. Electricity belongs to Technology)
    topics = jsonFile['summarizedInsights']['topics']
    profile = {} 
    profile['namedPeople'] = namedPeople
    profile['topics'] = topics
    return profile

  def search(self, searchWord) :
    vids = self.indexerClient.listVideos()['results']
    vidList = []
    for v in vids:
      if(-1 != v['name'].lower().find(searchWord.lower())):
        vidList.append(v['id'])
    returnJson = {}
    returnJson['vidlist'] = vidList
    return returnJson

   
# processor = Processor()
# bigJson = processor.getVideoById(TEST_VIDEO_ID)
# profile = processor.reformatJSON(bigJson)
# print(profile.keys())
