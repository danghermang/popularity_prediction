import csv
import inspect
import time

import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser

import TweeterParser
from init import TweeterWrapper as Init
from mop_files.internet_on import internet_on


def init_tweeter():
    TweeterWrapper = Init.TweeterConnection()
    auth = OAuthHandler(TweeterWrapper.get_consumer_key(), TweeterWrapper.get_consumer_secret())
    auth.set_access_token(TweeterWrapper.get_access_token(), TweeterWrapper.get_access_secret())
    api = tweepy.API(auth, parser=JSONParser())
    return api


def write_csv(current_user, tweets):
    with open('%s_tweets.csv' % current_user, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(tweets)
    pass


class CollectData(object):

    def __init__(self):
        if internet_on:
            self.api = init_tweeter()

    def collect_data(self, current_user):
        new_tweets = self.api.user_timeline(current_user)
        print(new_tweets)
        out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in new_tweets]
        write_csv(current_user, out_tweets)

    def user_tweets(self, user):
        if internet_on():
            return self.api.user_timeline(user)

    def user_friends_list(self, user):
        friends = []
        for user in tweepy.Cursor(self.api.friends, count=50, screen_name=user).items(50):
            friends.append(user)
        return friends

    def user_firends_list_v2(self, user):
        return self.api.friends(user)

    def user_friend_count(self, user):
        friends = self.user_friends_list(user)
        return len(friends)

    def user_follow_list(self, user):
        follow = []
        for user in tweepy.Cursor(self.api.followers, count=5000, screen_name=user).items():
            follow.append(user)
        return follow

    @staticmethod
    def send_to_parser(data):
        tweeter_parser = TweeterParser.ParseTweet(data)
        dict = tweeter_parser.parse_tweets()
        return dict

    def __getattribute__(self, name):
        returned = object.__getattribute__(self, name)
        now = time.strftime("%c")
        if inspect.isfunction(returned) or inspect.ismethod(returned):
            print('Method called ', returned.__name__, 'at', now)
        return returned


x = CollectData()
tweets_list = x.user_tweets("@realDonaldTrump")
print(tweets_list[0])
# x.user_follow_list("@realDonaldTrump")
