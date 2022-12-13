#!/usr/bin/python3
"""  using this REST API, for a given employee ID, returns information about his/her TODO """
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def gathe_data_api(id):
    """ Doc  """

    todos_count = 0
    todos_done = 0
    employee_name = None
    employee_id = 0

    resp = requests.get(users_url).json()


    for i in resp:
        if i['id'] == id:
            name = i['name']

if __name__ == "__main__":
    gathe_data_api()
