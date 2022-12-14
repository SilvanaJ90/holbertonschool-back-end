#!/usr/bin/python3
"""
output of user information
"""

import csv
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
    with open('{}.csv'.format(sys.argv[1]), 'w')as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(ourdata)


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
