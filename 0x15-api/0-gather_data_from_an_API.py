#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def get_todo_list(employee_id):
    """Retrieve and display TODO list progress for a given employee ID"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_info = requests.get(user_url).json()
    employee_name = user_info.get('name')
    if not employee_name:
        return print("Employee not found.")
    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    print(f"{employee_name}\
     is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print("\t", task.get('title'))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py employee_id")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_todo_list(employee_id)
