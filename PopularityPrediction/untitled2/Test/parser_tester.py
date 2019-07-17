import unittest

from data.collect_data import CollectData


class MyTestCase(unittest.TestCase):
    user = "@realDonaldTrump"

    def init_test(self):
        test = CollectData()
        tweets_list = test.user_tweets("@realDonaldTrump")
        tweets = test.send_to_parser(tweets_list)
        return tweets

    def test_tweet_favourite_count(self):
        tweets = self.init_test()
        for tweet in tweets:
            self.assertNotAlmostEquals(tweet.get('favorite_count'), 0)

    def test_tweet_like_count(self):
        tweets = self.init_test()
        for tweet in tweets:
            self.assertNotEqual(tweet.get('retweet_count'), 0)

    def test_tweet_list_friends(self):
        tweets = self.init_test()
        for tweet in tweets:
            self.assertNotEqual(tweet.get('friends_count'), 0)

    def test_tweet_text(self):
        tweets = self.init_test()
        for tweet in tweets:
            self.assertNotIsInstance(tweet.get('text'), int)

    def test_tweet_user(self):
        tweets = self.init_test()
        for tweet in tweets:
            self.assertIsNotNone(tweet.get('user'))

    def test_collect_data_user_friends_list(self):
        test = CollectData()
        self.assertIsNotNone(test.user_tweets(self.user))

    def test_collect_data_user_tweets(self):
        test = CollectData()
        self.assertIsNotNone(test.user_tweets(self.user))

    def test_collect_data_user_follow_list(self):
        test = CollectData()
        self.assertIsNotNone(test.user_follow_list(self.user))


if __name__ == '__main__':
    unittest.main()
