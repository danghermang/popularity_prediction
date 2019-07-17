import PopularityPrediction.data.collect_data as twit_api
import PopularityPrediction.neural_network.model as model
import matplotlib.pyplot as plt
import multiprocessing
import argparse
import json
import PopularityPrediction.agent as agent
from pprint import pprint


def worker(tweet_id, return_dict):
    return_dict[tweet_id] = agent.agent_for_tweet(tweet_id,10,1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Get popularity prediction for a certain twitter user.")
    parser.add_argument('user',action='store', type=str)
    parser.add_argument('-b', '--basic', action='store_true')
    parser.add_argument('-r', '--reparse', action='store_true')
    args = parser.parse_args()
    if args.basic:
        tweets = twit_api.user_tweets(args.user)
        pprint(tweets)
        processes = []
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        jobs = []
        info = {}
        for tweet in tweets:
            tweet_info = model.get_tweet_info(tweet['text'])
            info[tweet['tweet_id']] = tweet_info
            p = multiprocessing.Process(target=worker, args=(tweet['tweet_id'], return_dict))
            jobs.append(p)
            p.start()
        for proc in jobs:
            proc.join()
        result = {element:(info[element],return_dict[element]) for element in info.keys()}
        with open("result.json",'w') as f:
            json.dump(result,f)
    elif args.reparse:
        with open("result.json", "r") as f:
            result = json.load(f)
        for i, element in enumerate(result):
            tweet_info = result[element][0]
            agent_info = result[element][1]
            dates = [x[0][-5:] for x in agent_info]
            favorites = [x[1] for x in agent_info]
            retweets = [x[2] for x in agent_info]
            plt.subplot(1, 2, i%2+1)
            plt.plot(dates, retweets, marker='o', label='favorites')
            plt.gca().set_title(str(tweet_info['clean_tweet_analisys']))
            plt.xticks(rotation=60)
            # plt.xlabel('favorites')
            plt.legend()
            plt.grid()
            if i %2==1:
                plt.show()