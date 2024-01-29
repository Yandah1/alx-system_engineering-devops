#!/usr/bin/python3
'''Python script to export data in the CSV format.'''

import json
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            json_data = {
                    str(id): [
                        {
                            'task': todo.get('title'),
                            'completed': todo.get('completed'),
                            'username': user_name
                        }
                        for todo in todos
                        ]
                    }
            with open('{}.json'.format(id), 'w') as file:
                json.dump(json_data, file)
