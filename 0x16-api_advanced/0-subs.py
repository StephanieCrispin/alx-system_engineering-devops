#!/usr/bin/python3
"""Function to get all subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
  """Gets number of subs under a subreddit"""
  url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
  headers = {
    "User-Agent":"linux:0x16.api.advanced:v1.0.0 (by /u/No-Apartment7060)"
  }
  response = requests.get(url, headers=headers, Redirects=False)
  if response.status_code == 404:
    return 0
  result = response.json().get("data")
  return results.get("subscribers")
