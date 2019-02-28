import os
import requests as req
import tweepy

# config load
GITHUB_API = os.getenv('GITHUB_API')

TWITTER_CONFIG = {
    "consumer_key": os.getenv("T_CONSUMER_KEY"),
    "consumer_secret": os.getenv("T_CONSUMER_SEC"),
    "access_token": os.getenv("T_ACCESS_TOKEN"),
    "access_token_secret": os.getenv("T_ACCESS_TOKEN_SEC")
}


def getAPITwitter(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def filterIssue(item):
    """filterIssue for filter by body is not None
    :returns: Boolean

    """
    return str(item['body']) is not ''


def saveData(data):
    """TODO: Docstring for saveData.

    :dict:data
    :returns: bool

    """
    pass


def twit(item):
    try:
        print("Update status: {0}"
              .format(item['body']))
        API = getAPITwitter(TWITTER_CONFIG)
        API.update_status(item['body'])
        return True
    except Exception as e:
        raise e

    return False


try:
    result = req.get(GITHUB_API)
    resultJson = result.json()
    resultFiltered = list(filter(filterIssue, resultJson))
    postToTwitter = list(map(twit, resultFiltered))

except Exception as e:
    print(e)
    raise e
