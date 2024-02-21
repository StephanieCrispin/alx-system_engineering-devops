#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import requests
import sys

if __name__ == "__main__":
  api_url = "https://jsonplaceholder.typicode.com/"  
  employee = sys.argv[1]

  users = requests.get(api_url + "users").json()
  
  user_todos = requests.get(api_url + "todos", params={"userId": employee}).json()

  completed_user_todos = [t.get("title") for t in user_todos if t.get("completed") is True]
  print("Employee {} is done with ({}/{})".format(users.get("name"), len(completed_user_todos), len(user_todos)))
  print("\t {}".format(c) for c in completed_user_todos)
  