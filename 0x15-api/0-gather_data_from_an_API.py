#!/usr/bin/python3
"""
Retrieves data from an API
This script retrieves data from a given API endpoint and
prints information about a specified employee
"""
import sys
import requests

def gather_data_from_api(employee_id):
    """
    Retrieve information about a specified employee
    """
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for employee ID: {}".format(employee_id))
        return

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]

    employee_name = todos[0]['userId']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
