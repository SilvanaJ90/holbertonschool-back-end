#!/usr/bin/python3
"""
returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(id):
    """ func return inf api"""
    todos_count = 0
    todos_done = 0
    task = []

    resp = requests.get(todos_url).json()
    resp_user = requests.get(users_url).json()

    name = None
    for i in resp_user:
        if i['id'] == id:
            name = i['name']

    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        """print(todos_count)"""
        if (i['completed'] and i['userId'] == id):
            todos_done += 1
            task.append(i['title'])

    print('Employee {} is done with tasks({}/{}):'.format(
        name, todos_done, todos_count))
    for i in task:
        print('\t ' + i)


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
