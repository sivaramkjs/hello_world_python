import os
import statistics

print(os.getcwd())
print(dir(os))

# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use
# import shutil

# shutil.copy('text.txt', 'files/')

# File wildcards
import glob

print(glob.glob('*.py'))

# regex
import re

s = 'Hello! How are you?'
print(re.findall(r'[a-zA-Z]+', s))

import random

print(random.choice(['yes', 'no', 'maybe']))

a = range(50)
print(random.sample(a, 10))
print([x for x in a])

print(statistics.mean(a))
print(statistics.median(a))

# internet access
from urllib.request import urlopen

with urlopen('https://docs.python.org/3.14/') as response:
    for line in response:
        l = line.decode()
        if 'updated' in l:
            print(l.rstrip())

# dates and times
from datetime import date

now = date.today()
print(now)
print(now.strftime('%Y-%m-%d is %d %b %Y which is a %A in %B'))

dt = date(1991, 1, 1)
print((now - dt).days / 365)

# timers
import sys
from pathlib import Path

print(str(Path(__file__).parent / "classes"))
# add a directory to the current execution path for discovery of modules in the directory
sys.path.append(str(Path(__file__).parent / "classes"))

from timeit import Timer


def split_chunk(data, chunk_size=10):
    while len(data) >= chunk_size:
        yield data[:chunk_size]
        data = data[chunk_size:] if len(data) >= chunk_size else data
    else:
        yield data


print(f'{Timer("split_chunk([random.randint(1, 100) for _ in range(100)])",
               globals={'split_chunk': split_chunk, 'random': random}).timeit(1000):.4f} (seconds)')

import time

start = time.perf_counter()
for _ in range(1000):
    split_chunk([random.randint(1, 100) for _ in range(100)])
end = time.perf_counter()

elapsed = end - start
print(f'{elapsed:.4f} (seconds)')
