from __future__ import print_function
import twitter


class TwitterUser:
    def __init__(self, api: twitter.Api, twitter_user):
        self.api = api
        self.user = twitter_user
        self.screen_name = twitter_user.screen_name
        self.id = twitter_user.id
        self.following_count = twitter_user.friends_count
        self.follower_count = twitter_user.followers_count
        self.following_ids = []
        self.follower_ids = []

        self.fill_follow_ids()
        self.tweets = api.GetUserTimeline(screen_name=self.screen_name)


    def fill_follow_ids(self):
        self.following_ids = self.api.GetFriendIDs(user_id=self.id)
        self.follower_ids = self.api.GetFollowerIDs(user_id=self.id)

    @classmethod
    def create_by_sn(cls, api: twitter.Api, screen_name: str):
        tmp = api.GetUser(screen_name=screen_name)
        return cls(api, tmp)

    @classmethod
    def create_by_id(cls, api: twitter.Api, user_id: str):
        tmp = api.GetUser(user_id=user_id)
        return cls(api, tmp)

    def generate_relations(self):
        pass

    def to_dict(self):
        return {
            'id': self.id,
            'sn': self.screen_name,
            'fr_count': self.follower_count,
            'fg_count': self.following_count,
        }


class Relation:
    def __init__(self, api: twitter.Api, from_user: TwitterUser, to_user: TwitterUser):
        self.api = api
        self.from_user = from_user
        self.to_user = to_user
        self.weight = 0
        self.determine_weight()

    def determine_weight(self):
        self.weight = 0
        if self.from_user.id in self.to_user.following_ids:
            self.weight += 1
        if self.to_user.id in self.from_user.following_ids:
            self.weight += 1.3
