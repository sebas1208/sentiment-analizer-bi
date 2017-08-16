'''
 QUITO
==============
'''
import couchdb
import sys
import urllib2
import textblob
import datetime
import json

from couchdb import view
from textblob import TextBlob

from tweeterProcess import TweeterProcess

URL = 'localhost'
db_name = 'tweets_uio'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


#
# url = 'http://127.0.0.1:5984/tweets_uio/_design/quito/_view/quito'
# req = urllib2.Request(url)
# f = urllib2.urlopen(req)
# for x in f:
#     print(x)
# f.close()

view = "quito_view/quito_view"

LIMIT_OF_DOCUMENTS = 100000

tp = TweeterProcess()

fp = open('./Listas/horasTweets.json', 'r')
horas = json.load(fp)
fw = open('./Listas/horasTweets.json', 'w')

for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
    # print '=' * 40
    # print '====>', data['value']
    # print '---->', data['value'].split()
    tp.processTweet(data['value']['text'])
    
    if(tp.processTweet(data['value']['text'])[0] > 0):
        print data['value']['text']
        dt = datetime.datetime.fromtimestamp(float(data['value']['timestamp'])/1000.0)
        hour = str(dt.hour).encode('utf-8')
        horas[hour] += 1

print horas
fw.write(json.dumps(horas))
            # text_es = TextBlob(data['value'])
            # text_en = text_es.translate(to="en")
            # polarity_value = text_es.sentiment.polarity * 100.0
            # polarity = ""
            # if polarity_value == 0:
            #     polarity = 'neutral'
            # elif polarity_value < 0:
            #     polarity = 'negative'
            # else:
            #     polarity = 'positive'
            # subjectivity = text_es.sentiment.subjectivity
            # json_data['label'] = {'polarity': polarity, 'polarity_value': polarity_value, 'subjectivity': subjectivity}
            # try:
            #     db.save(json_data)
            # except:
            #     print "Data repeated..."


