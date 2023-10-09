# Author: Jet Semrick
# Date: 09-21-2023
# Problem: Write code to sum two lists by integer.
# Source: 2.5 from pg. 94 Cracking the Coding Interview

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def sum_lists(a,b):
  # Create another function to implement the carry
  return add_lists(a,b,0)

def add_lists(a,b,c):
  # Check for end of both lists
  if (not a and not b and not c):
    return None
  # Initialize value with the carry
  value = c
  if a:
    value += a.data
    a = a.next
  if b:
    value += b.data
    b = b.next

  # Eliminate the carry from the value
  solution = Node(value % 10)
  
  if a or b:
    # Recursive call to populate the list
    n = add_lists(a, b, value >= 10)
    solution.next = n

  return solution

def printlist(head):
  while(head.next):
    print(head.data, end="")
    head = head.next
  print(head.data, end="")

# Setting up test Linked ListS with  data
a = Node(1)
b = Node(5)
a_current = a
b_current = b

for i in range(4):
  a_current.next = Node(i)
  a_current = a_current.next

  b_current.next = Node(i)
  b_current = b_current.next

# 1 -> 0 -> 1 -> 2 -> 3 + 5 -> 0 -> 1 -> 2 -> 3
# Solution = 6 -> 0 -> 2 -> 4 -> 6
printlist(sum_lists(a,b))

