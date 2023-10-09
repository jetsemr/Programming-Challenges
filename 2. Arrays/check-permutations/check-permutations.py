# Author: Jet Semrick
# Date: 09-04-2023
# Problem: Implement a algorithm to deterine if one string is a permutation of another.
# Source: 1.2 from pg. 90 Cracking the Coding Interview

def checkPermutations(a,b):
  if len(a) != len(b):
    return False

  letters = {}
  for char in a:
    if char not in letters:
      letters[char] = 1
    else:
      letters[char] +=1
  for char in b:
    if char not in letters or letters[char] == 0:
      return False
    else:
      letters[char] -= 1
  return True

# Test Cases
print(checkPermutations("ab","ba") == True)
print(checkPermutations("a b","ba") == False)
print(checkPermutations("a","b") == False)
print(checkPermutations("ababab","bascd") == False)