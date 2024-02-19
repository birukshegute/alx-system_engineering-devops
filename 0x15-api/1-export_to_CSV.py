#!/usr/bin/python3
""" Records all tasks that are owned by this employee in CSV format.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE """

import requests
from sys import argv
import csv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url+'todos/')
    data = response.json()

    task = []
    response_2 = requests.get(url+'users/')
    data_2 = response_2.json()

    for i in data_2:
        if i['id'] == int(argv[1]):
            Employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    for i in data:

        task = []
        if i['userId'] == int(argv[1]):
            task.append(i['userId'])
            task.append(Employee)
            task.append(i['completed'])
            task.append(i['title'])

            writer.writerow(task)
