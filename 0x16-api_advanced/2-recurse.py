#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    query_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-Agent"},
                            allow_redirects=False)
    if query_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in query_info.json()
                        .get("data")
                        .get("children")]

    info = query_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))