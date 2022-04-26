#!/usr/bin/python3
"""Module that queries the reddit api"""


python = subreddit
def top_ten(python):
    """script that queries the Reddit API and returns the top 10 hot post
    to the subreddit"""
    import requests

    query_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(python),
                            headers={"User-Agent": "My-Agent"},
                            allow_redirects=False)
    if query_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in query_info.json().get("data").get("children")]