import tweepy
import sys
import json
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch
 
 
consumer_key='ZPUFJufusEHYf9Nv6288gYYJY'
consumer_secret='D5HbZsXijqhDJR0fmUZYiUsKF1h0zXpZlW6cjr4Z2bFJ1utG8g'
access_token_key='4909619429-27dq1xD9g8pDZeXPutig4aUY30vX2cdli1nOFKV'
access_token_secret='I5m0EaZ8zuFVzSKJNYKmRPXM7bDqLlzunbDxpQQRE9MCO'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
 
es = Elasticsearch()
 
class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
 
    def on_status(self, status):
        
        #print('n%s %s' % (status.author.screen_name, status.created_at))
        json_data=status._json
     #   print(status)
        
    #    twitdata = json.dumps(json_data)

        #this is twitter data in jason format. need to filter to get tweets that that 
        
        saveFile = open('twitDB2dat', 'a')
        saveFile.write(json.dumps(json_data)
        saveFile.write('\n')
        saveFile.close()
        
        #print("json Data length ", len(json_data))
        #print("json Data length ", len(json_data['results']))

       
        #twit = status.split(',"coordinates":')[1].split(',"place":')[0]
        #print("len of twit ", len(twit))              
        #print("twit", twit)
              
        if status.coordinates is "None":
            print("tweet null ")
            pass
        else:
            json_data = status._json
          #  print("json_data ", json_data)
            es.create(index="idx_twp",
                 doc_type="twitter_twp",
                 body=json_data
             )
            
          
#res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
#print(res['created'])

streamer = tweepy.Stream(auth=auth, listener=StreamListener())
streamer.filter(track=["Trump"])



