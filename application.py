#
from flask import Flask, request
from processor import Processor

from indexerclient import IndexerClient

app = Flask(__name__)
processor = Processor()

#front end requests
@app.route('/', methods=['GET'])
#
def parse_request():
  body = request.get_json(force=True)
  title = body['title']
  category = body['category']
  speaker = body['speaker']
  
  # print(body['phrase'])
    # processor.search(body['phrase'])
    # return 'testPhrase'
# def hello_world():
  return title





if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')