# Author: Jet Semrick
# Date: 10-18-2023
# Problem: Produce a stack that is ordered with min at the top. You can use another stack.
# Source: 3.5 from pg. 99 Cracking the Coding Interview

import sys
sys.path.append("..")
# pylint: disable=import-error
import structures

class SortedStack:
  def __init__(self):
    self.main = structures.Stack()
    self.helper = structures.Stack()
  
  def push(self, value):
    while (not self.main.isEmpty() and self.main.peek() < value):
       self.helper.push(self.main.pop())
    self.main.push(value)
    while (not self.helper.isEmpty()):
      self.main.push(self.helper.pop())
  
  def pop(self):
    return self.main.pop()
  
  def peek(self):
    return self.main.peek()

  def isEmpty(self):
    return self.main.isEmpty()
    

# Test Cases

s = SortedStack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek() == 1)
s.push(7)
s.push(8)
s.push(4)
s.pop()
print(s.peek() == 2)
s.push(5)
s.push(6)
print(s.peek() == 2)
s.pop()
print(s.peek() == 3)
