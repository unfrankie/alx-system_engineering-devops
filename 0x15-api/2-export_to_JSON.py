#!/usr/bin/python3
import sys
import json

def read_data_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("File not found:", filename)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error decoding JSON file:", filename)
        sys.exit(1)

def print_completed_tasks(data, user_id):
    user_tasks = [task['title'] for task in data if task['userId'] == user_id and task['completed']]
    if user_tasks:
        print("Completed tasks for user {}:".format(user_id))
        for task in user_tasks:
            print("\t{}".format(task))
    else:
        print("No completed tasks found for user {}.".format(user_id))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <input_file> <user_id>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]
    user_id = int(sys.argv[2])

    todo_data = read_data_from_json(input_file)
    print_completed_tasks(todo_data, user_id)
