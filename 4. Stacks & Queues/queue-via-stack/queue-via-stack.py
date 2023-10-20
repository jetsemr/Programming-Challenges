# Author: Jet Semrick
# Date: 10-10-2023
# Problem: Produce a queue using two stacks.
# Source: 3.4 from pg. 99 Cracking the Coding Interview

import sys
sys.path.append("..")
# pylint: disable=import-error
import structures

# Queue has FIFO order
class Queue:
  def __init__(self):
    self.size = 0
    self.old = structures.Stack()
    self.new = structures.Stack()

  def add(self, value):
    self.new.push(value)
    self.size += 1

  def remove(self):
    if (self.old.isEmpty()):
      while(not self.new.isEmpty()):
        self.old.push(self.new.pop())
    self.size -= 1
    return self.old.pop()

  def peek(self):
    if (self.old.isEmpty()):
      while(not self.new.isEmpty()):
        self.old.push(self.new.pop())
    return self.old.peek()

  def isEmpty(self):
    return self.size == 0

# Tests
queue = Queue()
print(queue.isEmpty() == True)
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove()
print(queue.peek() == 2)
queue.add(4)
queue.add(5)
print(queue.remove() == 2)
queue.remove()
queue.remove()
queue.remove()
print(queue.isEmpty() == True)

