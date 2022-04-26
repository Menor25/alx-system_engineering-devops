#!/usr/bin/python3
"""Module that queries the reddit api"""


def number_of_subscribers(subreddit):
    """script that queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    query_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if query_info.status_code >= 300:
        return 0

    return query_info.json().get("data").get("subscribers")