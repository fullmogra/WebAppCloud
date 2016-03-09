from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

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
