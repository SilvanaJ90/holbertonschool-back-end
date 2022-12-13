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
    task_completed = []

    resp = requests.get(todos_url).json()
    resp_user = requests.get(users_url).json()

    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        """print(todos_count)"""
        if (i['completed'] and i['userId'] == id):
            todos_done += 1
            task_completed.append(i['title'])

    print('Employee {} is done with tasks({}/{}):'.format(resp_user[1]['name'], todos_done, todos_count))
    for i in task_completed:
        print('\t ' + i)
   

if __name__ == "__main__":
    first_line(int(sys.argv[1]))
