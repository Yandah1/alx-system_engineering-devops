#!/usr/bin/python3
'''Python script to export data in the CSV format.'''

import csv
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_res = requests.get(f'{API_URL}/users/{user_id}').json()
            todos_res = requests.get(f'{API_URL}/todos').json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
