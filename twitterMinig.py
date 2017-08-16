'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "WN03Hf81cA7549Q2CPxVWYBMC"
csecret = "HyQMWqV6xZ5ImmtJjk0jY59irnyim14ow3s7d9T5bKoi3ieMxp"
atoken = "45447970-3yJGmuC1QsJZW1bDLbyl34hjOm9wenayCUFVt08gn"
asecret = "ttZCrRVFxXp8ECTOsZlnTasLygf3bnnJ5eRJzwam2HGF2"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #() poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''

twitterStream.filter(locations=[-78.593445,-0.370099,-78.386078,-0.081711])  #QUITO
