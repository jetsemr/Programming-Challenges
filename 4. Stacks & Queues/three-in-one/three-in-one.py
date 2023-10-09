# Author: Jet Semrick
# Date: 10-22-2023
# Problem: Implement three stacks into a single array.
# Source: 3.1 from pg. 98 Cracking the Coding Interview

class MultiStack:
  def __init__(self, stacksize):
    self.numstacks = 3
    self.array = [0] * (stacksize * self.numstacks)
    self.sizes = [0] * self.numstacks
    self.stacksize = stacksize

  def push(self, item, stacknum):
    if self.isFull(stacknum):
      raise Exception('Full!')
    self.sizes[stacknum] += 1
    self.array[self.indexOfTop(stacknum)] = item

  def pop(self, stacknum):
    if self.isEmpty(stacknum):
      raise Exception('Empty!')
    value = self.array[self.indexOfTop(stacknum)] = 0
    self.array[self.indexOfTop(stacknum)] = 0
    self.sizes[stacknum] -= 1
    return value

  def isEmpty(self, stacknum):
    return self.sizes[stacknum] == 0

  def isFull(self, stacknum):
    return self.sizes[stacknum] == self.stacksize

  def indexOfTop(self, stacknum):
    offset = stacknum * self.stacksize
    return offset + self.sizes[stacknum] - 1