
from observer.Observer import Observer


class User(Observer):
    _name = ''
    _tweets = []
    _tweetComments = []
    _reTweetsNumber = 0
    _tweeterFollowers = 0
    _tweeterFollowing = 0

    def __init__(self, name='', tweets=None, comments=None, reTweets=0, tweeterFollowers = 0, tweeterFollowing = 0):
        Observer.__init__(self)
        self._tweets = tweets
        self._name = name
        self._comments = comments
        self._reTweets = reTweets
        self._tweeterFolowers = tweeterFollowers
        self._tweeterFollowing = tweeterFollowing
        self.notify()
