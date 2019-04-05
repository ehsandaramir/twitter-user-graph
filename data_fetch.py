from __future__ import print_function
import twitter
import json

from api_data import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from models import *

if __name__ == '__main__':
    api = twitter.Api(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET,
        tweet_mode='extended',
        # sleep_on_rate_limit=True,
    )

    seed_screen_name = 'DevCampIUST'
    seed = TwitterUser.create_by_sn(api, seed_screen_name)
    # friends = [TwitterUser.create_by_id(api, user_id) for user_id in seed.following_ids]

    print('')
