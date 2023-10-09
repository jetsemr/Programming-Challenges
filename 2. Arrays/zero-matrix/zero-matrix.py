# Author: Jet Semrick
# Date: 09-12-2023
# Problem: Implement a algorithm to fill cols and rows with zero if a zero is detected in the col or row.
# Source: 1.8 from pg. 91 Cracking the Coding Interview

def zero(arr):
  cols = {}
  rows = {}
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if j not in rows:
        if arr[i][j] == 0:
          rows[j] = True
          cols[i] = True

  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if i in cols or j in rows:
        arr[i][j] = 0

  return arr

# Test Cases
arr = [[0,2,3,4],[1,2,3,4],[1,2,0,4]]
print(zero(arr) == [[0, 0, 0, 0], [0, 2, 0, 4], [0, 0, 0, 0]])
