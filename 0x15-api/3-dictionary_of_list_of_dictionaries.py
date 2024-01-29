#!/usr/bin/python3
'''Python script to export data in the JSON format.'''

import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(API_URL)).json()
    users = {user['id']: user['username'] for user in users_res}
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    tasks_by_user = {}
    for todo in todos_res:
        user_id = todo['userId']
        task = {
            'username': users[user_id],
            'task': todo['title'],
            'completed': todo['completed']
        }
        tasks_by_user.setdefault(str(user_id), []).append(task)
        
    with open('todo_all_employees.json', 'w') as file:
        json.dump(tasks_by_user, file)
