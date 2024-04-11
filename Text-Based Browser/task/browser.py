import argparse
import collections
import os

parser = argparse.ArgumentParser(description="This program is a text based browser in python.")
parser.add_argument("directory")
args = parser.parse_args()
if not os.access(args.directory, os.F_OK):
    os.makedirs(args.directory)

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

dns = {"nytimes.com": nytimes_com, "bloomberg.com": bloomberg_com}
open_tabs = []
current_tab = collections.deque()
for url in iter(input, 'exit'):
    if url in dns:
        print(dns.get(url.strip()))
        with open(os.path.join(args.directory, str(url.strip().split(".")[0])), 'w') as t:
            t.write(dns.get(url))
        open_tabs.append(str(url.split(".")[0]))
        current_tab.append(url)

    elif url in open_tabs:
        with open(os.path.join(args.directory, url), 'r') as t:
            print(t.read())
    elif url == 'back':
        try:
            current_tab.pop()
            print(dns.get(current_tab[-1].strip()))
        except IndexError:
            pass
    else:
        print("Error: Invalid URL")
