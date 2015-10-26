import os
import sys
import twitter
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from cassandra.cqlengine.connection import set_session
from models import Tweet
from datetime import datetime
import simplejson as json


CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
CASSANDRA_ADDRESS = [os.environ.get('CASSANDRA_ADDRESS', '127.0.0.1')]
CASSANDRA_KEYSPACE = os.environ.get('CASSANDRA_KEYSPACE')

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


if __name__=='__main__':
    cluster = Cluster(CASSANDRA_ADDRESS)
    session = cluster.connect(CASSANDRA_KEYSPACE)
    session.row_factory = dict_factory
    set_session(session)
    while True:
        with open('keywords.txt', 'r') as keywords:
            stream = api.GetStreamFilter(track=keywords.read().splitlines())
        for tweet in stream:
            geo_dict = tweet.get('geo')
            if geo_dict:
                geo_type = geo_dict.get('type')
                geo_coordinates = geo_dict.get('coordinates')
            else:
                geo_type = None
                geo_coordinates = None
            user = tweet.get('user')
            if user:
                user_id = user.get('id')
                user_name = user.get('name')
                user_screen_name = user.get('screen_name')
            Tweet.create(
                id=tweet.get('id'),
                text=tweet.get('text'),
                user_id=user_id,
                user_name=user_name,
                user_screen_name=user_screen_name,
                geo_type=str(geo_type),
                geo_coordinates=geo_coordinates,
                created_at=str(tweet.get('created_at', '')),
                raw_tweet=json.dumps(tweet)
            )
