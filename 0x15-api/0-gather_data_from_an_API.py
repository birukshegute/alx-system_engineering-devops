#!/usr/bin/python3
""" A Py script for a given employee ID, 
returns information about his/her TODO list progress """

import requests
from sys import argv


if __name__ == "__main__"
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url+'todos/')
    data = response().json
    done = 0
    total = 0
    task = []
    response_2 = requests.get(url+'users/')
    data_2 = response_2.json()

    for i in data_2:
        if i.get('id') == int(argv[1]):
            Employee = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            total+=1

            if i.get('completed') is True:
                done += 1
                task.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(Employee, done,
                                                          total))

    for i in task:
        print("\t {}".format(i))
