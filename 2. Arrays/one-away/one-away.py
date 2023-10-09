# Author: Jet Semrick
# Date: 09-07-2023
# Problem: Implement a algorithm to determine if two strings are one edit away.
# Source: 1.5 from pg. 91 Cracking the Coding Interview

def oneAway(a,b):
  diff = abs(len(a) - len(b))
  if diff > 1:
    return False
  if diff == 0:
    swap_count = 0
    for i in range(len(a)):
      if a == b:
        return True
      if a[i] != b[i]:
        swap_count += 1
      if swap_count > 1:
        return False
    return True
  if diff == 1:
    minLength = min(len(a), len(b))
    indexA = 0
    indexB = 0
    count = 0
    for i in range(minLength):
      if count > 1:
        return False
      if a[i] != b[i]:
        count += 1
        if len(a) > len(b):
          indexA += 1
        else:
          indexB += 1
      else:
        indexA += 1
        indexB += 1
    return True

# Test Cases
print(oneAway("aaab", "aaab") == True)
print(oneAway("acab", "aaab") == True)
print(oneAway("aacab", "aaab") == True)
print(oneAway("aaabasf", "aaab") == False)