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
            json_entry = {'task': i['title'], 'completed': i[
                'completed'], 'username': usr_resp[0]['username']}
            ourdata.append(json_entry)
            final_json = {str(i['userId']): ourdata}

    with open('{}.json'.format(sys.argv[1]), 'w')as f:
        f.write(json.dumps(final_json))


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
