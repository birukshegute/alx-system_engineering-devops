#!/usr/bin/python3
""" queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """ recursive function to perform the task"""
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    headers = {'User-Agent': 'CustomClient/1.0'}
    info = requests.get(url, headers=headers, allow_redirects=False)
    if info.status_code != 200:
        return (None)
    info = response.json()
    if "data" in response:
        data = info.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)
