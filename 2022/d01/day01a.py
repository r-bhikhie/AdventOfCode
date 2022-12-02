import math
import sys
from pprint import pprint

data = ''
sums = []

with open("input.txt", mode='r') as f:
    data = f.readlines()

#print(data)

cals = 0
highest_cal = 0
for line in data:
    if line != "\n":
        cals += int(line)
    else:
        if cals > highest_cal:
            highest_cal = cals
        cals=0
print(highest_cal)
        