#!/usr/bin/python3
"""
JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Doc """

    response = requests.get(todos_url).json()
    final_json = {}
    ourdata = []
    for i in response:
        url = users_url + str(i['userId'])
        usr_resp = requests.get(url).json()
        json_entry = {'username': usr_resp[0]['username'],
                        'task': i['title'], 'completed': i['completed']}
        ourdata.append(json_entry)
    final_json[str(i['userId'])] = ourdata

    with open("todo_all_employees.json", mode="w") as f:
        f.write(json.dumps(final_json))


if __name__ == "__main__":
    user_info()
