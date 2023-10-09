# Author: Jet Semrick
# Date: 09-19-2023
# Problem: Remove duplicates from a Linked List.
# Source: 2.1 from pg. 94 Cracking the Coding Interview

import random

# Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Setting up test Linked Lists with random data
head = Node(5)
current = head
for i in range(9):
  current.next = Node(random.randint(1,5))
  current = current.next

# Remove Duplicates algorithm
def remove_duplicates(head):
  # Check to see Linked List has data
  if head is None:
    return

  # Set to track seen data
  dups = set([head.data])
  current = head

  # Iterate through the list
  while current.next:
    if current.next.data in dups:
      # Set next to skip duplicated data
      current.next = current.next.next
    else:
      # Mark data as seen
      dups.add(current.next.data)
      current = current.next
  return head

def printlist(head):
  while(head.next):
    print(head.data, end="")
    head = head.next
  print(head.data, end="")

# Test Cases
printlist(head)
print("")
printlist(remove_duplicates(head))