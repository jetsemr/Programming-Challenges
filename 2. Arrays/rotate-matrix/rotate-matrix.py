# Author: Jet Semrick
# Date: 09-11-2023
# Problem: Implement a algorithm to rotate a matrix 90 degrees.
# Source: 1.7 from pg. 91 Cracking the Coding Interview

def rotate_matrix(arr, n):
  for i in range(n):
    for j in range(i):
      temp = arr[i][j]
      arr[i][j] = arr[j][i]
      arr[j][i] = temp
  for i in range(n):
    for j in range(int(n/2)):
      temp = arr[i][j]
      arr[i][j] = arr[i][n - j - 1]
      arr[n - j - 1][i] = temp
  return arr

arr = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
print(arr)
print(rotate_matrix(arr, 6))