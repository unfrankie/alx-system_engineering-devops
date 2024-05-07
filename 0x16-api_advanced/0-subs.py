#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
