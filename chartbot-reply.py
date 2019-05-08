from twython import Twython, TwythonError, TwythonStreamer
import time
import random 



print("Listening for tweets...")

APP_KEY = "1hrm6Lx9xIpnSd0PwvShPbPAb"
APP_SECRET = "7s84kpy5vfZ5e3nndiVgT5fNcFpyKdt0NFwpkS6vBxCN0wpsmV"
OAUTH_TOKEN = "1102317081943371776-I2e51UOtkTTbjsuvi2Z6X89wyH6thn"
OAUTH_TOKEN_SECRET = "3maEMfLf8MtuTrmGgZKgb70ifjbK64fACP7tofhoMPSpn"


def twitter_api():

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return twitter

def reply(data):

    api = twitter_api()
    tweet_text = data.get('text')
    handle = data.get('user').get('screen_name')
    tweet_id = data.get('id')

    responses = ["How do you find stock picks?"]
    response = random.choice(responses)

    if tweet_text[0] != "@" and "RT" not in tweet_text:
        try:
            time.sleep(1)
            api.update_status(status = f"@{handle}  {response}", in_reply_to_status_id=tweet_id)
            print(f"Reply sent to {handle}'s tweet")
        except TwythonError as e:
            print(e)
    else:
        print(f"This tweet '{tweet_text}' is probably a reply or retweet")

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        # screenName = data.get('user').get('screen_name') 
        tweetText = data.get('text') 
        # chatResponse = chatbot.respond(tweetText)
        print(tweetText)
        reply(data)
       
    def on_error(self, status_code, data):
        print("Twitter Error Status code", status_code)

        # self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track = ["stock trading",])
