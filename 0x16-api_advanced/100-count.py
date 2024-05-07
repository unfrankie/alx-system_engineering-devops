#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses titles of hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively counts the occurrences of given keywords
    in titles of hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    word_count[word] = word_count.get(word, 0) + 1
        if data['data']['after'] is not None:
            return count_words(subreddit, word_list, data['data']['after'],
                               word_count)
        else:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        print(None)
