#!/usr/bin/python3

import random

size = 10000
for k in range(50):
  f = open('graph' + str(k) + '.tgf', 'w')
  edge_chance = 7



  for x in range(size):
    print(str(x) + ' ' + str(x), file=f)  

  print('#', file=f)

  for x in range(size):
    for y in range(size):
      if x != y and random.randrange(size) < edge_chance:
        print(str(x) + ' ' + str(y), file=f)

  f.close()
