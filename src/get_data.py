import os
from dotenv import load_dotenv
import json, requests
import tweepy as tw
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import random
import pandas as pd


load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


locations = [-125,25,-65,50]
locations_alaska = [-167.958984375,52.10650519075632,-141.15234374999997 ,71.99257805093251]
location_hawaii = [-161.1474609375,18.312810846425442,-153.78662109375,22.958393318086348]
location_p_rico = [-67.5384521484375,17.54977183258917,-65.0885009765625,18.869904894964883]
languages = ['en','sp']

# This is a class to get tweeits on streaming with no other filter than the language or the location:

class listener(StreamListener):
    def __init__(self,max_tw,csv_name):
        super().__init__()
        self.max_tweets = max_tw
        self.tweet_count = 0
        self.tweet_id=[]
        self.date=[]
        self.tweet=[]    
        self.lat=[]
        self.lon=[]
        self.csv_name=csv_name
    def on_status(self, status):
        self.tweet_count+=1
        text = status.text
        if(self.tweet_count==self.max_tweets):
            print("completed")
            return(False)
        else:
            try:
                coords.update(status.coordinates)
                lat_lon = (coords.get('coordinates')) 
            except:
                bounding = status.place.bounding_box.coordinates[0]                                    
                lat_lon = [(bounding[0][0] + bounding[2][0])/2, (bounding[0][1] + bounding[2][1])/2]
            self.tweet_id.append(status._json['id'])
            self.date.append(status._json['created_at'])
            self.lat.append(lat_lon[1])
            self.lon.append(lat_lon[0])
            if not status.truncated:
                self.tweet.append(status._json['text'])
            else:
                self.tweet.append(status._json['extended_tweet']['full_text'])
            
            result = {"tweet_id":self.tweet_id,"date":self.date,'latitude':self.lat,'longitude':self.lon,'tweet':self.tweet}       
        return pd.DataFrame(result).to_csv(self.csv_name)

# This function is linked with the class:
def call_tweets(max_tweets,locations,languages,csv_name):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    twitterStream = Stream(auth, listener(max_tweets,csv_name))
    twitterStream.filter(locations=locations,languages=languages)
    return 'completed'


# This function get 100 x number of loops wanted of tweets with a key word wherever you want with a radius.

geocode='39.758286,-101.428189,3000km'
def api_search_loop(csv_name,loops,key_word,geocode):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True) 
    tweet_id=[]
    date=[]
    tweet=[]    
    location=[]
    for j in range(loops):
        usa = api.search(q=key_word, lang="en",geocode=geocode, tweet_mode = "extended", max_results=100)
        for i in usa:
            tweet_id.append(i._json['id'])
            date.append(i._json['created_at'])
            tweet.append(i._json['full_text'])
            location.append(i._json["user"]['location'])
    result = {"tweet_id":tweet_id,"date":date,'location':location,'tweet':tweet}       
    return pd.DataFrame(result).to_csv(csv_name)




