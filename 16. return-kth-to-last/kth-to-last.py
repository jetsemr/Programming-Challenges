# Author: Jet Semrick
# Date: 09-19-2023
# Problem: Return the Kth to last value in a Linked List
# Source: 2.2 from pg. 94 Cracking the Coding Interview

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
def kth_to_last(head, k):
  if head == None:
    return 0
  
  index = kth_to_last(head.next, k) + 1

  if index == k:
    print(head.data)

  return index

# Setting up test Linked List with  data
head = Node(1)
current = head
for i in range(2,11):
  current.next = Node(i)
  current = current.next

kth_to_last(head, 1)
kth_to_last(head, 5) 
kth_to_last(head, 9) 