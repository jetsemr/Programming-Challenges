# Author: Jet Semrick
# Date: 10-03-2023
# Problem: There is a max stack height. If exceeded, create a new stack. This should operate like a single stack. 
# Source: 3.3 from pg. 99 Cracking the Coding Interview

import sys
sys.path.append("..")
# pylint: disable=import-error
import structures

class PlateStack:
  def __init__(self, maxSize):
    self.arr = [structures.Stack()]
    self.maxSize = maxSize
    self.size = 0

  def push(self, value):
    currIndex = len(self.arr) - 1
    if self.arr[currIndex].size == self.maxSize:
      self.arr.append(structures.Stack())
      currIndex += 1
    self.arr[currIndex].push(value)
    self.size += 1

  def pop(self):
    currIndex = len(self.arr) - 1
    val = self.arr[currIndex].pop()
    self.size -= 1
    if currIndex != 0 and self.arr[currIndex].isEmpty():
      self.arr.pop()
    return val
  
  def peek(self):
    currIndex = len(self.arr) - 1
    return self.arr[currIndex].peek()
  
  def isEmpty(self):
    return self.arr[0].isEmpty()
  
  def getSize(self):
    return self.size

# Test Cases
s = PlateStack(2)
print(s.isEmpty())
for i in range(10):
  s.push(i)

print(s.peek() == 9)
print(s.pop() == 9)
print(s.getSize() == 9)