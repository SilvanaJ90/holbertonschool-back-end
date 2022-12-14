#!/usr/bin/python3
"""
JSON output
"""

import json
import requests


users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Doc """

    resp = requests.get(todos_url).json()
    resp_user = requests.get(users_url).json()

    final_json = {}
    
    for i in resp_user:
        ourdata = []
        for j in resp:

            json_entry = {'username': resp_user[0]['username'],
                          'task': j['title'], 'completed': j['completed']}
            if i['id'] == j['userId']:
                ourdata.append(json_entry)
        final_json[str(i['id'])] = ourdata

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(final_json))


if __name__ == "__main__":
    user_info()
