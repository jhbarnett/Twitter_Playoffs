import requests
from requests_oauthlib import OAuth1Session
import time


def fetch_tweets(query):
    # Request
    # GET https://api.twitter.com/1.1/search/tweets.json

    try:
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params={
            "q": query,
            "result_type": "mixed",
            "count": 100,
            "include_entities": False
        }
        twitter = OAuth1Session('wLZpuBiSJOwefMtj5JQNQYF55', 'WGPayLiNNl7u9atZMmKWdyFJWd9ucU1Mr0BeviiZaWS3rFTAFl',
                      '2744454516-jCPIngVTt8z7QVyfjYtv0LStygdKWPos2gYwQ6F', 'Y5H617Jay8mRz0AH9IYOpaXz3k35XUZ8uUyAhKgqAx5V4')

        response = twitter.get(url, params=params)

        print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        json = response.json()
        return parse_tweets(json)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def parse_tweets(r):
    tweets = r['statuses']
    data = list(map(lambda x: {
        'user': x['user']['name'],
        'user_url': x['user']['url'],
        'user_image': x['user']['profile_image_url'],
        'text': x['text'],
        'created_at':
            time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(x['created_at'], '%a %b %d %H:%M:%S +0000 %Y')),
        'retweet_count': x['retweet_count'],
        'favorites_count': x['favorite_count']
    }, tweets))
    return data
