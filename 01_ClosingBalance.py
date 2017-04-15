#!/usr/local/bin/python3.5

from unittest import *
from functools import reduce

input = '''93174
5
-834
735
-345
-642
-182'''

print(reduce(lambda x, y : x + y, map(int, input.split("\n"))) - int(input.split("\n")[1]))
