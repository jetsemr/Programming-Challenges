# Author: Jet Semrick
# Date: 7-22-2022
# Problem: Write a function that concatenates two lists in alternating ways.

def joinListsAlts(arr1, arr2):
  array = []
  for n in arr1:
    array.append(n)
    array.append(arr2[arr1.index(n)])
  return array

print (joinListsAlts([1,2,3],[4,5,6]))