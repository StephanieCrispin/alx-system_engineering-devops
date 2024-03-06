#!/usr/bin/python3
"""Function to get a list of top 10 titles in a subreddit"""
import requests

def top_ten(subreddit):
  """Gets number of subs under a subreddit"""
  url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
  headers = {
    "User-Agent":"linux:0x16.api.advanced:v1.0.0 (by /u/No-Apartment7060)"
  }
  params = {
    "limit":10
  }
  response = requests.get(url, headers=headers, params=params, Redirects=False)

  if response.status_code == 404:
    return 0
  result = response.json().get("data")
  [print(c.get('data').get('title') for c in result.get('children'))]
  