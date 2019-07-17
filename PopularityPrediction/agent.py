import PopularityPrediction.data.collect_data as twit_api
import PopularityPrediction.neural_network.model as model
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
import argparse
import time
import datetime
import json
from pprint import pprint


def agent_for_tweet(tweet_id, tries, times):
    tweet_evolution = []
    for i in range(tries):
        tweet = twit_api.twit_info(tweet_id)
        tweet_evolution.append([datetime.datetime.now().strftime("%x\n%X"),
                                tweet.retweet_count, tweet.favorite_count])
        print("got twit info at", str(datetime.datetime.now()))
        time.sleep(times*60)
    return tweet_evolution


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Get popularity prediction for a certain twitter user.")
    parser.add_argument('twit_id', action='store', type=str)
    parser.add_argument('-r', '--tries', action='store', type=int,default=50)
    parser.add_argument('-t', '--time', action='store', type=int, default=1)
    parser.add_argument('-b', '--basic', action='store_true')
    args = parser.parse_args()
    if args.basic:
        # tweet_evolution = []
        # tweet = twit_api.twit_info(args.twit_id)
        # text = tweet.text
        # for i in range(args.tries):
        #     tweet = twit_api.twit_info(args.twit_id)
        #     tweet_evolution.append([datetime.datetime.now().strftime("%x\n%X"),
        #                             tweet.retweet_count, tweet.favorite_count])
        #     print("got twit info at", str(datetime.datetime.now()))
        #     time.sleep(args.time*60)
        # with open("output.json",'w') as f:
        #     json.dump({"text": text, "tweet_id": args.twit_id, "tweet_evolution": tweet_evolution}, f)
        # plt.text(0.5, 0.5, "Twit: "+text, horizontalalignment='center', verticalalignment='center')
        with open("output.json") as f:
            obiect = json.load(f)
        print(obiect["text"])
        tweet_evolution = [element for i,element in enumerate(obiect["tweet_evolution"]) if i%3==0]
        times = [x[0] for x in tweet_evolution]
        retweets = [x[1] for x in tweet_evolution]
        likes = [x[2] for x in tweet_evolution]
        plt.subplot(2, 1, 1)
        plt.plot(times, retweets, marker='o', label='retweets')
        plt.gca()
        plt.xlabel('time')
        plt.ylabel('retweets')
        plt.legend()
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.plot(times, likes, marker='o', label='likes')
        plt.gca()
        plt.xlabel('time')
        plt.ylabel('likes')
        plt.legend()
        plt.grid()
        plt.show()

