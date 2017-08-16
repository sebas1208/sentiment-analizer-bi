from flask import Flask, jsonify
from tweeterProcess import TweeterProcess
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__, static_url_path='/Listas')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

tp = TweeterProcess()

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/horas')
@cross_origin()
def horas():
    with open('./Listas/horasTweets.json') as horas_file:
        _horas = json.load(horas_file)
    return jsonify(_horas)

@app.route('/general')
@cross_origin()
def general():
    with open('./Listas/generalTweets.json') as horas_file:
        _horas = json.load(horas_file)
    return jsonify(_horas)

@app.route('/processTweet/<tweet>')
@cross_origin()
def processTweet(tweet):
    return jsonify(tp.processTweet(tweet))

if __name__ == '__main__':
   app.run()