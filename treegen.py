#!/usr/bin/python3

import random

size = 100000
f = open('tree.tgf', 'w')
b_factor = 7



for x in range(size):
  print(str(x) + ' ' + str(x), file=f)  

print('#', file=f)

queue = [0]
current = 1

while current < size:
  level = queue.pop(0)
  for x in range(b_factor):
    if(current >= size):
      break
    print(str(level) + ' ' + str(current), file=f)
    queue.append(current)
    current = current + 1

print('14806 5', file=f)
