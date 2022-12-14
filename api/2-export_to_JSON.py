#!/usr/bin/python3
"""
output of user information
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Doc """
    total_tasks = 0
    response = requests.get(todos_url).json()
    ourdata = []
    for i in response:
        if i['userId'] == id:
            url = users_url + str(i['userId'])
            usr_resp = requests.get(url).json()
            line = str(i['userId']), usr_resp[0]['username'], str(
                i['completed']), i['title']
            ourdata.append(line)

    student_json = json.dumps(ourdata)
    with open('{}.json'.format(sys.argv[1]), 'w')as f:
        f.write(student_json)


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
