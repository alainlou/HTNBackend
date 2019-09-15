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
  word = request.args.get('searchWord')
  # name  = request.args.get('searchWord')
  return processor.getTopFive(word)

#search uses keywords to return a bunch of video urls
@app.route('/search', methods=['GET'])
@cross_origin()
def search():
  parsed_url = urlparse.urlparse(request.url)
  searchWord = urlparse.parse_qs(parsed_url.query)['searchWord'][0]
  return processor.search(searchWord)

@app.route('/topFive', methods=['GET'])
@cross_origin()
def getTopFive():
  return processor.getTopFive()

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
  word = request.args.get('searchWord')
  return processor.getVideoURL(word)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='8080')
>>>>>>> 4ebccda... some changes
# end of front end requests

# run this to get data and sort into json things

# bigJson = processor.getVideoById(TEST_VIDEO_ID)
# print(processor.organizeByKeywords(bigJson))



