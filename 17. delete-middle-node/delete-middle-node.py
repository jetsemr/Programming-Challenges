# Author: Jet Semrick
# Date: 09-20-2023
# Problem: Delete a node from the middle of a Linked List given only access to that node.
# Source: 2.3 from pg. 94 Cracking the Coding Interview

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def delete_middle_node(middle):
  if (middle == None or middle.next == None):
    return False
  middle.data = middle.next.data
  middle.next = middle.next.next
  return True

def printlist(head):
  while(head.next):
    print(head.data, end="")
    head = head.next
  print(head.data, end="")

# Setting up test Linked List with  data
head = Node(1)
current = head
for i in range(2,11):
  current.next = Node(i)
  current = current.next

# Test Cases
printlist(head)
print('\n')
middle = head
for i in range(5):
  middle = middle.next
delete_middle_node(middle)
printlist(head)


