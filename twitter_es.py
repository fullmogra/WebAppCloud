import tweepy
import sys
import json
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()
 
consumer_key='XXX'
consumer_secret='XXX'
access_token_key='XXX'
access_token_secret='XXX'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
 
class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
 
    def on_status(self, status):
        
        json_data=status._json
        
        for tweet in json_data:
            # to check if this has location info
            if tweet in ["coordinates"]:
                value = json_data[tweet]
                if value is not None :
                   # print("Not null coordinates values are ({}) = ({})".format(tweet, value))
                    saveFile = open('twitDB2_coord.dat', 'a')
                    saveFile.write(json.dumps(json_data))
                    saveFile.write('\n')
                    saveFile.close()

                    es.create(index="idx_twp",
                             doc_type="twitter_twp",
                             body=json_data
                             )
                else:
                    pass
             
streamer = tweepy.Stream(auth=auth, listener=StreamListener())
streamer.filter(track=["Trump", "Hillary Clinton", "Ted Cruz"])



