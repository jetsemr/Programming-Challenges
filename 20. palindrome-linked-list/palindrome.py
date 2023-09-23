# Author: Jet Semrick
# Date: 09-23-2023
# Problem: Implement a function to check if a linked list is a palindrome.
# Source: 2.6 from pg. 94 Cracking the Coding Interview

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def is_palindrome(a):
  b = reverse_list(a)
  return isEqual(a, b)

def reverse_list(a):
  head = None
  while a:
    # New node with data
    n = Node(a.data)
    # Set new node next to one ahead
    n.next = head
    # Set new head
    head = n
    # Iterate
    a = a.next
  return head

def isEqual(a,b):
  while a and b:
    if a.data != b.data:
      return False
    a = a.next
    b = b.next
  return a == None and b == None