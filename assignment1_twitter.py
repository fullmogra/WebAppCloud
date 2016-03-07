from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key='ZPUFJufusEHYf9Nv6288gYYJY'
consumer_secret='D5HbZsXijqhDJR0fmUZYiUsKF1h0zXpZlW6cjr4Z2bFJ1utG8g'
access_token_key='4909619429-27dq1xD9g8pDZeXPutig4aUY30vX2cdli1nOFKV'
access_token_secret='I5m0EaZ8zuFVzSKJNYKmRPXM7bDqLlzunbDxpQQRE9MCO'

class listener(StreamListener):

    def on_data(self, data):
        #try:
            #print(data)
            '''
            saveFile = open('twitDB.dat', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            '''
            #my_string="hello python world , i'm a beginner "
            #>>> print(my_string.split("hello ",1)[1].split("world ")[0] )
            #python 

            twit = data.split(',"coordinates":')[1].split(',"place":')[0]
            print(len(data))
            
            print("coordinates ", text)
            
            print("twit", twit)
            print(len(twit))
                  

            if twit.strip() is "null":
                print("tweet null ")
                pass
            else:
                '''  es.create(index="idx_twp",
                 doc_type="twitter_twp",
                 body=json_data
                 )
                '''
                saveFile = open('cleantwitDB.dat', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
     
            return True
       # except BaseException:
        #    print('failed on data')
         #   time.sleep(5)
        

    def on_error(self, data):
        return status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])
                            
#api = tweepy.API(auth)
