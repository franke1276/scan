import sys
import logging
import httplib2
from flask import Flask
from flask import Response
from flask import render_template
from flask import make_response
from flask import request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=['GET'])
def index():
  return render_template('index.html', event_type="scans")


@app.route("/", methods=['PUT'])
def put_data():
  global data
  d = request.args.get('data', '')
  sse.publish({"message": d}, type='scans')
  return make_response("OK", 200)

def scan():
  logging.info("Start listen to barcode scanner.")
  while 1:
    line = sys.stdin.readline().rstrip()
    logging.debug("got from scanner: {}".format(line))
    # h = httplib2.Http()
    # resp, content = h.request("http://heise.de/", "GET")
