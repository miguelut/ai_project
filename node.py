#!/usr/bin/python3

class Node:
  
  def __init__(self, num):
    self.num = int(num)
    self.succ = []
    self.pred = []

  def __str__(self):
    return str(self.num) + '\n' + str(self.succ) + '\n' + str(self.pred)

  def addSucc(self, succ):
    self.succ.append(succ)

  def addPred(self, pred):
    self.pred.append(pred)

