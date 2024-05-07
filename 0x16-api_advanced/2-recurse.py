#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns
a list containing titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': hot_list[-1] if hot_list else None}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            recurse(subreddit, hot_list)
        return hot_list
    return None
