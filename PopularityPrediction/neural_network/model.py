import csv
import pickle
import re


from textblob.sentiments import NaiveBayesAnalyzer
from textblob.sentiments import PatternAnalyzer
from pprint import pprint

# import keras

pattern_analyzer = PatternAnalyzer()
bayes_analyzer = NaiveBayesAnalyzer()
link_pattern = r"((http|ftp|https):\/\/)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
tag_pattern = r"@[\w]*"
emoji_pattern = r"(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)"
non_char_pattern = r"^[\W]+"
white_spaces_pattern = r"^[\s]|$[\s]"


def csv_to_pickle(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            reader = csv.reader(f)
            lista = list(reader)
            tags = [element[0] for element in lista]
            tweets = [element[1:] for element in lista]
            with open(output_path, 'wb') as fb:
                pickle.dump((tweets, tags), fb)
        return True
    finally:
        return False


def load_pickle_file(input_path):
    pickle_in = open(input_path, "rb")
    return pickle.load(pickle_in)


def get_tweet_info(tweet):
    result = {'tags': re.findall(tag_pattern, tweet),
              'links': re.findall(link_pattern, tweet),
              'emojis': re.findall(emoji_pattern, tweet),
              'original_tweet': tweet,
              'original_tweet_analisys': get_tweet_sentiment(tweet, bayes=False),
              'clean_tweet': clean_tweet(tweet),
              }
    result['clean_tweet_analisys'] = get_tweet_sentiment(result['clean_tweet'], bayes=False)
    return result


def clean_tweet(tweet):
    # regex for detecting links
    tweet = re.sub(link_pattern, "", tweet)
    # regex for detecting tags
    tweet = re.sub(tag_pattern, "", tweet)
    # regex for detecting emojis
    tweet = re.sub(emoji_pattern, "", tweet)
    # regex for detecting non-word characters
    tweet = re.sub(non_char_pattern, "", tweet)
    # removing white spaces at the start or end of the text
    tweet = re.sub(white_spaces_pattern, "", tweet)
    return tweet


def tags_in_tweet(tweet):
    pattern = "@[\w]+"
    for element in re.findall(pattern, tweet):
        print(element)
    print(len(re.findall(pattern, tweet)))


def get_tweet_sentiment(tweet, bayes=False):
    if bayes:
        return bayes_analyzer.analyze(tweet)
    return pattern_analyzer.analyze(tweet)


# csv_to_pickle('training.csv', 'training.pickle')
# fisier = load_pickle_file('training.pickle')
# values={}
# for element in fisier[0][100000:100040]:
#     polarity, subjectivity = get_tweet_sentiment(element[4])
#     print(element[4], polarity, subjectivity)
# print(values)
if __name__ == "__main__":
    text = "@switchfoo3t http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"
    print(text)
# print(get_tweet_sentiment(text, bayes=False))
# print(clean_tweet(text))
# print(get_tweet_sentiment(clean_tweet(text), bayes=False))
    pprint(get_tweet_info(text))