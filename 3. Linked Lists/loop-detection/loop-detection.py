# Author: Jet Semrick
# Date: 09-27-2023
# Problem: Implement a function to check if a linked list has a loop.
# Source: 2.8 from pg. 94 Cracking the Coding Interview

def loop_detection(head):
  # Vars to race through the list
  fast = head
  slow = head

  if not head:
    return False

  # Race
  while fast is not slow:
    if not fast.next or not fast.next.next:
      return False
    # Fast moves at 2K
    fast = fast.next.next
    # Slow moves at K
    slow = slow.next
  
  # collision = mod(k, LOOP_SIZE)
  fast = head
  while fast is not slow:
    fast = fast.next
    slow = slow.next
  return fast