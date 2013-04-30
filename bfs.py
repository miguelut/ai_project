#!/usr/bin/python3

#Breadth-frist search.
from node import Node

def bfs(nodes,start, goal):
  queue = []
  paths = []
  visited = set()

  queue.append(nodes[start])
  paths.append([nodes[start]])

  while not len(queue) == 0:
    node = queue.pop(0)
    path = paths.pop(0)
    if str(node.num) == goal:
      return path
    else:
      for n in node.succ:
        if n not in visited:
          visited.add(n)
          queue.append(n)
          paths.append(path + [n])

