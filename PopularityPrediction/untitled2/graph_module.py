import matplotlib.pyplot as plt
import numpy as np

from data.collect_data import CollectData

x = CollectData()
tweets_list = x.user_tweets("@realDonaldTrump")
tweets = x.send_to_parser(tweets_list)


def like_array():
    like = []
    for tweet in tweets:
        if tweet.get('favorite_count') != 0:
            like.append(tweet.get('favorite_count'))
    return like


def re_tweet_array():
    retweet = []
    for tweet in tweets:
        if tweet.get('retweet_count') != 0:
            retweet.append(tweet.get('retweet_count'))
    return retweet


def tweet_graph(array, type):
    min_array = np.min(array)
    max_array = np.max(array)
    fig = plt.figure()

    fig.subplots_adjust(bottom=0.2)

    ax1 = fig.add_subplot(211)

    line1 = ax1.plot(array, 'bo-', label=str(type) + ' evolution')

    ax1.set_ylim(min_array - 1000, max_array + 1000)

    lines = line1
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc=(0, -0.4), ncol=5)
    plt.show()


tweet_graph(np.array(like_array()), "like")
tweet_graph(np.array(re_tweet_array()), "retweet")
