#
from flask import Flask, request
from flask_cors import CORS, cross_origin

from processor import Processor
from indexerclient import IndexerClient

import urllib.parse as urlparse

TEST_VIDEO_ID = '198c26215e'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

processor = Processor()

@app.route('/', methods=['GET'])
@cross_origin()
def info():
  name  = request.args.get('name')
  return processor.process(name)

# front end requests
@app.route('/video', methods=['GET'])
@cross_origin()
def parse_request():
  # body = request.get_json(force=True)
  
  #bc we're using params
  parsed_url = urlparse.urlparse(request.url)
  searchWord = urlparse.parse_qs(parsed_url.query)['searchWord'][0]
  returnJson = processor.organizeByKeywords(searchWord)
  return(returnJson)
  # return(urlparse.parse_qs(parsed_url.query)['searchWord'])
#   title = body['title']
#   category = body['category']
#   speaker = body['speaker']

# run this to get data and sort into json thingsbigJson = processor.getVideoById(TEST_VIDEO_ID)
  profile = processor.reformatJSON(bigJson)
  print(profile.keys())
# print(profile)

@app.route('/test', methods=['GET'])
@cross_origin()
def test():
  return processor.test()

@app.route('/refresh', methods=['GET'])
@cross_origin()
def refresh():
  processor.refresh()
  return "OK"
# run this to get data and sort into json thingsbigJson = processor.getVideoById(TEST_VIDEO_ID)
profile = processor.reformatJSON(bigJson)
print(profile.keys())
# print(profile)

<<<<<<< HEAD
#if __name__ == '__main__':
#  app.run(debug=True, host='0.0.0.0', port='8080')
=======
@app.route('/video', methods=['GET'])
@cross_origin()
def video():
  return processor.getVideoURL()

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='8080')
>>>>>>> 4ebccda... some changes
# end of front end requests

# run this to get data and sort into json things

# bigJson = processor.getVideoById(TEST_VIDEO_ID)
# print(processor.organizeByKeywords(bigJson))



