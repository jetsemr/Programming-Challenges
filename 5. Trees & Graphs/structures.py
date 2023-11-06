# Author: Jet Semrick
# Date: 10-23-2023
# Problem: Tree and graph structures.
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Graph:
  def __init__(self):
    self.adjacencyList = {}
  
  def addVertice(self, node):
    self.adjacencyList[node.value] = []

  def addEdge(a, b):
    self.adjacencyList[a].append(b)
    self.adjacencyList[b].append(a)
