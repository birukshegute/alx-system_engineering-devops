#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/dev/api.json".format(subreddit)
    headers = {"User-Agent": "Headers"}
    info = requests.get(url, headers=headers)

    if info.status_code != 200: 
        return (0)
    info = info.json()
    return (info.json().get("data").get("subscribers"))
