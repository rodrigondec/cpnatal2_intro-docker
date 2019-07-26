from os import environ
from time import sleep
import logging

from requests import get

logging.basicConfig(level=logging.DEBUG)

# Server url
URL = f'http://{environ.get("HOST_URL", "localhost")}:8000/'
logging.debug(f'Host url for request: {URL}')

n = 1
if __name__ == '__main__':
    while True:
        # sending get request and saving the response as response object
        logging.debug(f'Making request number {n}...')
        r = get(url=URL, params={'name': f'requester {n}'})
        logging.debug(f'Request number {n} returned {r}')
        logging.debug(f'Response received: {r.text}')
        n += 1
        logging.debug('sleeping for 3 seconds...')
        sleep(3)
