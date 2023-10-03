# Author: Jet Semrick
# Date: 10-03-2023
# Problem: There is a max stack height. If exceeded, create a new stack. This should operate like a single stack. 
# Source: 3.3 from pg. 99 Cracking the Coding Interview

class Stack:

  def __init__(self, size):
    self.size = size
  def push(self, item):
    return -1
  def pop(self):
    return -1

stacks = []
capacity = 10
def push(item):
  # curr should get last stack
  curr = None
  if not curr.isFull():
    curr.push()
  else:
    stack = Stack(capacity)
    stack.push(item)
    stacks.append(stack)

def pop():
  # last should get last stack
  last = None
  last.pop()
  if last.size == 0:
    stacks.pop(len(stacks) - 1)