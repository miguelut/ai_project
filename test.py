#!/usr/bin/python3

from node import Node
from bfs import bfs
from dfs import dfs
from dldfs import dldfs
from iddfs import iddfs
from bidir import bidir
import time

o = open('results.txt', 'w')

def timeit(f, start, goal, k):
  t1 = time.time()
  result = f(nodes,start,goal)
  t2 = time.time()
  if result != None:
    result = len(result) 
  print('%d\t%s\t%s\t%0.6f s' % (k, str(result),f.__name__,t2-t1), file=o)

for k in range(50):
  nodes = dict()
  f = open('graph' + str(k) + '.tgf', 'r')
  

  line = f.readline()
  while line[0] != '#':
    nodes[line.split()[0]] = Node(line.split()[0])
    line = f.readline()

  for line in f.readlines():
    nodes[line.split()[0]].addSucc(nodes[line.split()[1]])
    nodes[line.split()[1]].addPred(nodes[line.split()[0]])

  f.close()

  timeit(bfs,'0','9999',k)
  timeit(dfs,'0','9999',k)
  timeit(dldfs,'0','9999',k)
  timeit(iddfs,'0','9999',k)
  timeit(bidir,'0','9999',k)


