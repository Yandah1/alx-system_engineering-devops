#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers'''

import requests


def number_of_subscribers(subreddit):
    '''Get the number of subscribers'''
    headers = {'user-Agent': 'MyBot/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error:{response.status_code}")
        return 0
