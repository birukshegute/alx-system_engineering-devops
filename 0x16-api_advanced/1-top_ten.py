#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts """

import requests


def top_ten(subreddit):
    """A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    info = requests.get(url, headers=headers)
    if info.status_code != 200:
        return 0
    else:
        [print(child.get("data").get("title"))
         for child in info.json().get("data").get("children")]
