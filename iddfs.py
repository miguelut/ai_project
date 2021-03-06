#!/usr/bin/python3

#Iterative deepening depth-first search
from node import Node

def iddfs(nodes,start, goal):
  max_lim = 200
  limit = 1
  while(limit <= max_lim):
    stack = []
    paths = []
    stack.append(nodes[start])
    paths.append([nodes[start]])

    while not len(stack) == 0:
      node = stack.pop()
      path = paths.pop()
      visited = set(path)
      if str(node.num) == goal:
        return path
      elif (len(path) < limit):
        for n in node.succ:
          if n not in visited:
            stack.append(n)
            paths.append(path + [n])
    limit = limit + 1

