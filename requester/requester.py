from os import environ
from time import sleep

from requests import get

# Server url
URL = environ.get('HOST_URL', 'http://0.0.0.0:8000/')

n = 1

if __name__ == '__main__':
    while True:
        # sending get request and saving the response as response object
        r = get(url=URL, params={'name': f'requester {n}'})
        print(f'Request number {n} made! response received: {r.text}')
        n += 1
        print('sleeping for 3 seconds...')
        sleep(3)
