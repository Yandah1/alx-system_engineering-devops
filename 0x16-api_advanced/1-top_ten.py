#!/usr/bin/python3
'''
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
'''

import requests


def top_ten(subreddit):
    '''gets 10 hottest posts of a subreddit'''
    headers = {'User-Agent': 'test23'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
