import random

def find_max(a, l, r):
  print(l,r)
  # if l surpasses r, return system minimum
  if l > r:
    return float('-inf')
  # if l equals r, return the element
  if l == r:
    print(a[l])
    return a[l]
  # find the middle index
  mid = (l + r) // 2

  # divide the problem in half and continue
  left_max = find_max(a, l, mid)
  right_max = find_max(a, mid + 1, r)


  return max(left_max, right_max)

# create an array of length ten with random integers
array = [random.randint(0, 100) for _ in range(10)]
print(array)
max_value = find_max(array, 0, len(array) - 1)
print("Maximum value:", max_value)
