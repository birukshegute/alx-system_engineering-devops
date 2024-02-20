#!/usr/bin/python3
""" Python script to export data in the JSON format.
Records all tasks from all employees"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url+"users").json()
    data = {}
    for user in users:
        Id = user.get("id")
        username = user.get("username")
        tasks = requests.get(url+"users/{}/todos".format(Id)).json()
        task = [{"username": username,
                 "task": task.get("title"),
                 "completed": task.get("completed"),
                 } for task in tasks]
        data[Id] = task
    with open("todo_all_employees.json", 'w') as filejs:
        json.dump(data, filejs)
