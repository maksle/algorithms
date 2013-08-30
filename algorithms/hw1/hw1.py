#!/usr/bin/env python

import os
from .. import counting_inversions as ci

file_loc = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_loc)
os.getcwd()

integers = []

with open('IntegerArray.txt', 'rb') as ints:
    for i in ints:
        integers.append(int(i))

# should be 2407905288
print ci.count_inversions2(integers[:100])
