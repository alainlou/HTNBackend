from flask import Flask, request
from processor import Processor

app = Flask(__name__)
processor = Processor()

@app.route('/', methods=['GET'])
def search():
    body = request.get_json(force=True)
    # processor.search(body['phrase'])
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0')