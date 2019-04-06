from __future__ import print_function
import twitter
import json

from api_data import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from models import *


def create_api():
    api = twitter.Api(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET,
        tweet_mode='extended',
        # sleep_on_rate_limit=True,
    )
    return api


seed_screen_name = 'DevCampIUST'

