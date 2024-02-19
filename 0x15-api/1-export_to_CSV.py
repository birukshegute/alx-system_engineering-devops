#!/usr/bin/python3
""" Records all tasks that are owned by this employee in CSV format.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE """

import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    Id = argv[1]
    response = requests.get(url+"users/{}".format(Id))
    username = response.json().get('username')
    if username is not None:
        tasks = requests.get(url+"users/{}/todos".format(Id)).json()
    with open("{}.csv".format(Id), 'w', newline='') as csvfile:
        writeFile = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writeFile.writerow([int(Id),
                                   username,
                                   task.get('completed'),
                                   task.get('title')])
