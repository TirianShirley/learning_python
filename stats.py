#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
for line in fileinput.input():
	if line.startswith('#'): continue
	line = line.rstrip()
	data.append(float(line))
data.sort()
min = data[0]
max = data[-1]
sum = 0
for i in range(len(data)):
	sum += data[i]
mean = sum/len(data)
ssum = 0
for x in data:
	ssum += (mean - x)**2
std = sqrt(ssum/len(data))
median = None
if len(data) % 2 == 1:
	mi = int(len(data)/2)
	median = data[mi]
else:
	hi = int(len(data)/2)
	lo = hi -1
	median = (data[lo] + data[hi])/2
print(f'Count: {len(data)} ')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {sum/len(data)} ')
print(f'Std. dev: {std:.3f} ')
print(f'Median: {median}')
"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
