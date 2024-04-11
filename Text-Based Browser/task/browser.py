import argparse
import os

import requests

parser = argparse.ArgumentParser(description="This program is a text based browser in python.")
parser.add_argument("directory")
args = parser.parse_args()
if not os.access(args.directory, os.F_OK):
    os.makedirs(args.directory)

for url in iter(input, 'exit'):
    if '.' in url:
        if 'https://' not in url:
            url = 'https://' + url
        response = requests.get(url)
        response_text = response.text
        print(response_text)
        with open(os.path.join(args.directory, str(str(url.split('.')[0]).split('//')[1])), 'w') as t:
            t.write(response_text)
    elif os.access(os.path.join(args.directory, url), os.F_OK):
        with open(os.path.join(args.directory, url), 'r') as t:
            print(t.read())
    else:
        if url != 'back':
            print('Invalid URL')
