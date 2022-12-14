#!/usr/bin/python3
"""
JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Doc """

    response = requests.get(todos_url).json()
    ourdata = []
    for i in response:
        if i['userId'] == id:
            usr_resp = requests.get(users_url + str(i['userId'])).json()
            json_entry = {'username': usr_resp[0]['username'], 'completed': i['completed'], 'task': i['title']}
            ourdata.append(json_entry)

    student_json = json.dumps(ourdata)
    with open('{}.json'.format(sys.argv[1]), 'w')as f:
        f.write(student_json)


if __name__ == "__main__":
    user_info(int(sys.argv[1]))


