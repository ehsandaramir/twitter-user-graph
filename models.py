from __future__ import print_function
import twitter


class TwitterUser:
    all_users = []
    api = None

    def __init__(self, twitter_user):
        TwitterUser.all_users.append(self)

        self.user = twitter_user
        self.screen_name = twitter_user.screen_name
        self.id = twitter_user.id

        self.following_count = twitter_user.friends_count
        self.follower_count = twitter_user.followers_count
        self.following_ids = []
        self.follower_ids = []

        self.relation_to = []
        self.relation_from = []

        self.fill_follow_ids()

    def fill_follow_ids(self):
        self.following_ids = self.api.GetFriendIDs(user_id=self.id)
        self.follower_ids = self.api.GetFollowerIDs(user_id=self.id)

    @classmethod
    def create_instance(cls, twitter_user):
        for user in cls.all_users:
            if user.screen_name == twitter_user.screen_name:
                return user
        return cls(twitter_user)

    @classmethod
    def create_by_sn(cls, screen_name: str):
        tmp = cls.api.GetUser(screen_name=screen_name)
        return cls.create_instance(tmp)

    @classmethod
    def create_by_id(cls, user_id: str):
        tmp = cls.api.GetUser(user_id=user_id)
        return cls.create_instance(tmp)

    def to_dict(self):
        return {
            'id': self.id,
            'sn': self.screen_name,
            'follower_count': self.follower_count,
            'following_count': self.following_count,
        }


class Relation:
    api = None

    def __init__(self, from_user: TwitterUser, to_user: TwitterUser):
        self.from_user = from_user
        self.to_user = to_user
        self.weight = 0

        from_user.relation_to.append(self)
        to_user.relation_from.append(self)

        self.determine_weight()

    @classmethod
    def create_by_user_and_id(cls, user_from: TwitterUser, user_to: int):
        fetch_user = TwitterUser.create_by_id(user_to.__str__())
        return cls(user_from, fetch_user)

    def determine_weight(self):
        self.weight = 0
        if self.from_user.id in self.to_user.following_ids:
            self.weight += 1
        if self.to_user.id in self.from_user.following_ids:
            self.weight += 1.3


def configure_models(api: twitter.Api):
    TwitterUser.api = api
    Relation.api =api
