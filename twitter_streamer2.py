from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


import json
#Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXX"
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

class StdOutListener(StreamListener):
        def on_data(self, data):
                fhOut.write(data)
                j=json.loads(data)
                text=j["text"]
                print(text)
        def on_error(self, status):
                print(status)

if __name__ == '__main__':
        try:

                fhOut = open("myData.json","a")

                listener = StdOutListener()
                auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
                stream = Stream(auth, listener)

                stream.filter(track=['python', 'javascript', 'ruby'])
        except KeyboardInterrupt:
                 pass

        fhOut.close()





 

