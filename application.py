#
from flask import Flask, request
from processor import Processor

from indexerclient import IndexerClient

TEST_VIDEO_ID = '198c26215e'

app = Flask(__name__)
processor = Processor()

# front end requests
@app.route('/', methods=['GET'])

def parse_request():
  body = request.get_json(force=True)
  # title = body['title']
  # category = body['category']
  # speaker = body['speaker']

  #use this to test getting the entire json stats object thing for a video (WITH POSTMAN)
  bigJson = processor.getVideoById(TEST_VIDEO_ID)
  return bigJson
  # return processor.organizeByKeywords(bigJson)

if __name__ == '__main__':
  # app.run(debug=True, host='0.0.0.0')
  app.run(host='127.0.0.1', port=8080, debug=True)
# end of front end requests

# run this to get data and sort into json things

# bigJson = processor.getVideoById(TEST_VIDEO_ID)
# print(processor.organizeByKeywords(bigJson))



