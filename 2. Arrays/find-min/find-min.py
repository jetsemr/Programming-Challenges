import random

def find_min(a, l, r):
  """Given an array of nums find the minimum value using a divide and conquer approach."""
  # if l surpass r, return system maximim
  if l > r:
    return float('inf')
  # if l equals r, return the element
  if l == r:
    return a[l]
  
  mid = (l + r) // 2

  left_min = find_min(a, l, mid)
  right_min = find_min(a, mid+1, r)

  return min(left_min, right_min)

# create an array of length ten with random integers
array = [random.randint(0, 100) for _ in range(10)]
print(array)
max_value = find_min(array, 0, len(array) - 1)
print("Minimum value:", max_value)
