# Author: Jet Semrick
# Date: 10-17-2022
# Description: Stack data structure using nodes.

class Node:
 def __init__(self, value):
  self.value = value
  self.next = None
 
class Stack:
  def __init__(self):
    self.head = Node("head")
    self.size = 0
  def getSize(self):
    return self.size
  def isEmpty(self):
    return self.size == 0
  def peek(self):
    if self.isEmpty():
      raise Exception("Peeking empty stack")
    return self.head.next.value
  def push(self, value):
    node = Node(value)
    node.next = self.head.next
    self.head.next = node
    self.size += 1
  def pop(self):
    if self.isEmpty():
      raise Exception("Popping empty stack")
    remove = self.head.next
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.value
  
