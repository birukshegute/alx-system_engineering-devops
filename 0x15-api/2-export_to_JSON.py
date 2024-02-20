#!/usr/bin/python3
""" Python script to export data in the JSON format.
Records all tasks that are owned by this employee"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    Id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url+"users/{}".format(Id)).json()
    username = user.get('username')
    tasks = requests.get(url+"users/{}/todos".format(Id)).json()
    task = [{"task": task.get("title"),
             "completed": task.get("completed"),
             "username": username} for task in tasks]
    data = {}
    data[Id] = task
    with open("{}.json".format(Id), 'w') as filejs:
        json.dump(data, filejs)
