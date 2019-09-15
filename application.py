#
from flask import Flask, request
from flask_cors import CORS, cross_origin

from processor import Processor
from indexerclient import IndexerClient

TEST_VIDEO_ID = '198c26215e'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

processor = Processor()

@app.route('/', methods=['GET'])
@cross_origin
def info():
  return processor.clean()

# front end requests
@app.route('/video', methods=['GET'])
@cross_origin()
def parse_request():
#   body = request.get_json(force=True)
#   title = body['title']
#   category = body['category']
#   speaker = body['speaker']

  #use this to test getting the entire json stats object thing for a video (WITH POSTMAN)
#   bigJson = processor.getVideoById(TEST_VIDEO_ID)
#   return processor.organizeByKeywords(bigJson)
  return processor.getVideoURL()

@app.route('/refresh', methods=['GET'])
@cross_origin()
def refresh():
  processor.refresh()
  return "OK"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='8080')
# end of front end requests

# run this to get data and sort into json things

# bigJson = processor.getVideoById(TEST_VIDEO_ID)
# print(processor.organizeByKeywords(bigJson))



