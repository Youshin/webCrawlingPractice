import requests
from requests_oauthlib import OAuth1

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}'.format('naver_d2')

response = requests.get(url=url, auth=oauth)
statuses = response.json()
# print(statuses)

for status in statuses:
    print(status['text'],status['created_at'])
