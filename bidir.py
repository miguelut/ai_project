#!/usr/bin/python3

from node import Node

def bidir(nodes,start, goal):
  f_queue = []
  f_paths = []
  f_visited = set()

  b_queue = []
  b_paths = []
  b_visited = set()

  f_queue.append(nodes[start])
  f_paths.append([nodes[start]])

  b_queue.append(nodes[goal])
  b_paths.append([nodes[goal]])

  while not (len(f_queue) == 0 or len(b_queue) == 0):
    f_node = f_queue.pop(0)
    f_path = f_paths.pop(0)

    b_node = b_queue.pop(0)
    b_path = b_paths.pop(0)
    if set(f_path) & set(b_path) != set():
        shared = set(f_path) & set(b_path)
        f_index = f_path.index(list(shared)[0])
        b_index = b_path.index(list(shared)[0])
        return f_path[:f_index] + b_path[b_index:]
    else:
      for n in f_node.succ:
        if n not in f_visited:
          f_visited.add(n)
          f_queue.append(n)
          f_paths.append(f_path + [n])
      for n in b_node.pred:
        if n not in b_visited:
          b_visited.add(n)
          b_queue.append(n)
          b_paths.append([n] + b_path)

