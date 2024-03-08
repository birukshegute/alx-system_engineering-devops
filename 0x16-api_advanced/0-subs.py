#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and returns the number of subscribers"""
    info = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if info.status_code >= 300:
        return 0

    return info.json().get("data").get("subscribers")
