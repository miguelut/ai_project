#!/usr/bin/python3

#Depth limited depth-first search
from node import Node

limit = 7

def dldfs(nodes,start, goal):
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


