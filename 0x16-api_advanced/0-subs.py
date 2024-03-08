#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and returns the number of subscribers"""
    url = ("https://www.reddit.com/dev/api/{}/about.json"
           .format(subreddit))
    headers = {"User-Agent": "CustomClient/1.0"}
    info = requests.get(url, headers=headers, allow_redirects=False)

    if info.status_code != 200:
        return (0)
    info = info.json()
    if 'data' in info:
        return (info.json().get("data").get("subscribers"))

    else:
        return (0)
