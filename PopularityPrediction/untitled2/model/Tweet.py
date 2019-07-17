class Tweet:
    _tweets = []
    _likeTweet = []
    _retweet = []

    def __init__(self,tweets=None,likeTweet=None,retweet=None):
        self._tweets = tweets
        self._likeTweet = likeTweet
        self._retweet = retweet