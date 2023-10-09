# Author: Jet Semrick
# Date: 09-21-2023
# Problem: Write code to partition a linked list such that all nodes less than x come before all nodes greater than or equal to x. 
# Source: 2.4 from pg. 94 Cracking the Coding Interview

import random

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def partition(node, x):

  # Nodes w/ value less than x
  leftEnd = None
  leftHead = None

  # Nodes w/ value greater than or equal to x
  rightEnd = None
  rightHead = None

  while node:
    if node.data >= x:
      if rightEnd == None:
        rightEnd = node
        rightHead = rightEnd
      else:
        rightEnd.next = node
        rightEnd = rightEnd.next
    else:
      if leftEnd == None:
        leftEnd = node
        leftHead = leftEnd
      else:
        leftEnd.next = node
        leftEnd = leftEnd.next
    # Move to next node to sort
    node = node.next

  # Connect the two linked lists
  leftEnd.next = rightHead
  rightEnd.next = None

  if leftHead == None:
    return rightHead

  return leftHead

def printlist(head):
  while(head.next):
    print(head.data, end="")
    head = head.next
  print(head.data, end="")

# Setting up test Linked Lists with random data
head = Node(5)
current = head
for i in range(9):
  current.next = Node(random.randint(1,9))
  current = current.next

# Test Cases
printlist(head)
print('\n')
printlist(partition(head, 5))

1243596566