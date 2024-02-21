#!/usr/bin/python3
import requests
import json

"""Exports to-do list information of employee to JSON format"""

if __name__ == "__main__":
  url = "https://jsonplaceholder.typicode.com/"  
  users = requests.get(url + users).json()

  with open("todo_all_employee.json", "w") as jsonfile:
      with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
            