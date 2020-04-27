#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!
count = i
data = []
for line in fileinput.input():
	if line.startswith('#'): continue
	line = line.rstrip()
	data.append(float(line))
data.sort()
min = data[0]
max = data[-1]



print(f'Count: {count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: ')
print(f'Std. dev: ')
print(f'Median: ')
"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
