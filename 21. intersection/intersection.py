# Author: Jet Semrick
# Date: 09-26-2023
# Problem: Implement a function to check if two singly linked lists intersect.
# Source: 2.7 from pg. 94 Cracking the Coding Interview

def intersection(a,b):
  aLength = 1
  aHead = 0
  bLength = 1
  bHead = 0

  # A
  while a.next:
    aLength += 1
    a = a.next
  # B
  while b.next:
    bLength += 1
    b = b.next

  # Check if intersection
  if a is not b:
    return False

  # Reset a and b to head
  a = aHead
  b = bHead

  # Find intersection
  cut = aLength - bLength
  for _ in range(abs(cut)):
    if cut > 0:
      a = a.next
    else:
      b = b.next
  while a is not b:
    a = a.next
    b = b.next
  return a
    
    