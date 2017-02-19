from flask import Flask
from flask_rq2 import RQ


app = Flask(__name__)
app.config['RQ_LOW_URL'] = 'redis://localhost'
rq = RQ(app)

@rq.job
def process(i):
  3

process.delay(3)