tweeter_date = 'created_at'
tweeter_text = 'text'
tweeter_user = 'user'
tweeter_user_followers_count = 'followers_count'
tweeter_user_friends_count = 'friends_count'
tweeter_user_current_post_retweet_number = 'retweet_count'
tweeter_user_current_post_like_number = 'favorite_count'

keys = [tweeter_date, tweeter_text, tweeter_user, tweeter_user_followers_count, tweeter_user_current_post_retweet_number,
        tweeter_user_friends_count, tweeter_user_current_post_like_number]


class ParseTweet:
    tweets = ""

    def __init__(self, tweets):
        self.tweets = tweets

    def parse_tweets(self):
        list_dict = []
        for tweet in self.tweets:
            d = dict((k, 2) for k in keys)
            d[keys[0]] = tweet[tweeter_date]
            d[keys[1]] = tweet[tweeter_text]
            d[keys[2]] = tweet[tweeter_user]['name']
            d[keys[3]] = tweet[tweeter_user][tweeter_user_followers_count]
            d[keys[4]] = tweet[tweeter_user_current_post_retweet_number]
            d[keys[5]] = tweet[tweeter_user][tweeter_user_friends_count]
            d[keys[6]] = tweet[tweeter_user_current_post_like_number]
            list_dict.append(d)

        return list_dict
