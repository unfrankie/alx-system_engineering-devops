#!/usr/bin/python3
import sys
import requests
import json

def gather_data_from_api(employee_id):
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for employee ID: {}".format(employee_id))
        return

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]

    employee_name = todos[0]['userId']  # Assuming employee name is not provided in API

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

    return todos

def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data exported to", filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <employee_id> <output_file>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    output_file = sys.argv[2]

    todo_data = gather_data_from_api(employee_id)
    export_to_json(todo_data, output_file)
