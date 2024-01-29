import sys
import re
import requests
import csv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            
            # Print the title of each completed task
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
            
            # Export the data to a CSV file
            filename = '{}.csv'.format(id)
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
                for todo_done in todos_done:
                    writer.writerow([id, user_name, "Completed", todo_done.get('title')])
            
            print('Data exported to {}'.format(filename))
