#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main__":
  api_url = "https://jsonplaceholder.typicode.com/"  
  employee = sys.argv[1]
  user = requests.get(api_url + "user/{}".format(employee)).json()
  username = user.get("username")
  todos = requests.get(api_url + "todos", params={"userId": employee}).json()

  with open("{}.csv".format(employee), "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow([user_id, username, t.get("completed"), t.get('title')]) for t in todos]
    