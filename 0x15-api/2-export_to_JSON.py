#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export employee's tasks to JSON file"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_info = requests.get(user_url).json()
    employee_name = user_info.get('username')
    if not employee_name:
        return print("Employee not found.")
    tasks_data = {employee_id: []}
    for task in todos:
        tasks_data[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(tasks_data, json_file)
    print(f"Tasks exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py employee_id")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
