import time
from pprint import pprint

import tweepy
from tweepy import OAuthHandler
from PopularityPrediction.init import TweeterWrapper as Init
import csv
import json


def init_tweeter():
    TweeterWrapper = Init.TweeterConnection()
    auth = OAuthHandler(TweeterWrapper.get_consumer_key(), TweeterWrapper.get_consumer_secret())
    auth.set_access_token(TweeterWrapper.get_access_token(), TweeterWrapper.get_access_secret())
    api = tweepy.API(auth)
    return api


def collect_data(current_user):
    api = init_tweeter()
    new_tweets = api.user_timeline(current_user)
    # print(new_tweets)
    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in new_tweets]
    write_csv(current_user, out_tweets)


def write_csv(current_user, tweets):
    with open('%s_tweets.csv' % current_user, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(tweets)
    pass


# collect_data("@realDonaldTrump")
api = init_tweeter()


# print(str(api.user_timeline("")))


def user_tweets(user, count=20):
    new_tweets = api.user_timeline(screen_name=user, count=count)
    # print(new_tweets)
    out_tweets = [
        {'tweet_id': tweet.id_str, 'created_at': tweet.created_at, 'text': tweet.text, 'retweet': tweet.retweet_count,
         'favorite': tweet.favorite_count} for tweet in new_tweets]
    return out_tweets


def user_friends_list(user):
    friends = []
    for user in tweepy.Cursor(api.friends, count=50, screen_name=user).items(50):
        friends.append(user)
    return friends


def user_friend_count(user):
    friends = user_friends_list(user)
    return len(friends)


def user_follow_list(user):
    follow = []
    for user in tweepy.Cursor(api.followers, count=5000, screen_name=user).items():
        follow.append(user)
    return follow


def twit_info(twit):
    return api.get_status(twit)
