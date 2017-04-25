import requests
from requests_oauthlib import OAuth1Session


def send_request():
    # Request
    # GET https://api.twitter.com/1.1/search/tweets.json

    try:
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params={
            "q": "#NBAPlayoffs2017 OR #NBAPlayoffs",
            "result_type": "mixed",
        }
        twitter = OAuth1Session('wLZpuBiSJOwefMtj5JQNQYF55', 'WGPayLiNNl7u9atZMmKWdyFJWd9ucU1Mr0BeviiZaWS3rFTAFl',
                      '2744454516-jCPIngVTt8z7QVyfjYtv0LStygdKWPos2gYwQ6F', 'Y5H617Jay8mRz0AH9IYOpaXz3k35XUZ8uUyAhKgqAx5V4')

        response = twitter.get(url, params=params)

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')