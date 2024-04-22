#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        td_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        todos = requests.get(td_url).json()

        user_tasks = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task)

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)
