import unittest

from collect_data import *


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        list_tweets = user_tweets(api.get_user("@realDonaldTrump"))
        self.assertNotEqual([], list_tweets)

    def test_tweets_user(self):
        list_tweets = user_tweets(api.get_user("@realDonaldTrump"))
        self.assertNotEqual([], list_tweets)

    def test_friends_count(self):
        number_followers = user_friends_list(api.get_user("@realDonaldTrump"))
        self.assertNotEqual(0, number_followers)

    def test_friends_list(self):
        likes_list = user_friends_list(api.get_user("@realDonaldTrump"))
        self.assertNotEqual([], likes_list)


if __name__ == '__main__':
    unittest.main()
