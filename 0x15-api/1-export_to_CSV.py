#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export employee's tasks to CSV file"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_info = requests.get(user_url).json()
    employee_name = user_info.get('username')
    if not employee_name:
        return print("Employee not found.")
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                             employee_name,
                             task.get('completed'),
                             task.get('title')
                            ])
    print(f"Tasks exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py employee_id")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
