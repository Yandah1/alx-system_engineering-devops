#!/usr/bin/python3
'''Python script to export data in the CSV format.'''

import csv
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


def export_to_csv(user_id, user_name, todos):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"]
            })


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_res = requests.get(f'{API_URL}/users/{user_id}').json()
            todos_res = requests.get(f'{API_URL}/todos').json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == user_id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))

            print(f'Employee {user_name} is done with tasks({len(todos_done)}/{len(todos)}):')
            for todo_done in todos_done:
                print(f'\t {todo_done.get("title")}')
            
            # Export to CSV
            export_to_csv(user_id, user_name, todos_done)
            print(f'Data exported to {user_id}.csv')
