#!/usr/bin/python3

from node import Node
from bfs import bfs
from dfs import dfs
from dldfs import dldfs
from iddfs import iddfs
from bidir import bidir
import time

nodes = dict()
f = open('graph.tgf', 'r')

line = f.readline()
while line[0] != '#':
  nodes[line.split()[0]] = Node(line.split()[0])
  line = f.readline()

for line in f.readlines():
  nodes[line.split()[0]].addSucc(nodes[line.split()[1]])
  nodes[line.split()[1]].addPred(nodes[line.split()[0]])

def timeit(f, start, goal):
  t1 = time.time()
  result = f(nodes,start,goal)
  t2 = time.time()
  print('Elapsed time %0.6f s' % (t2-t1))
  if result != None:
    result = list(map(lambda x: x.num, result))
  print(result)
  
timeit(bfs,'0','9999')
timeit(bfs,'0','2764')

timeit(dfs,'0','9999')
timeit(dfs,'0','2764')

timeit(dldfs,'0','9999')
timeit(dldfs,'0','2764')

timeit(iddfs,'0','9999')
timeit(iddfs,'0','2764')

timeit(bidir,'0','9999')
timeit(bidir,'0','2764')

