#!/usr/bin/python3
'''
a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of
igiven keywords (case-insensitive, delimited by spaces.
'''

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''return count of keywords in hot posts titles'''
    user_agent = {'User-Agent': 'test45'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        data = response.json()['data']
        aft = data['after']
        posts = data['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            found_list.sort()
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
