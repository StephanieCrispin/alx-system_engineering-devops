#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
  api_url = "https://jsonplaceholder.typicode.com/"  
  employee = sys.argv[1]
  user = requests.get(api_url + "user/{}".format(employee)).json()
  username = user.get("username")
  todos = requests.get(api_url + "todos", params={"userId": employee}).json()

  with open("{}.json".format(user_id), "w") as jsonfile:
    json.dumps({
      user_id:[
        {
          "task":t.get('title'),
          "completed":t.get("completed"),
          "username":t.get("useername")
        } for t in todos
      ]
    }, jsonfile)
    