# Author: Jet Semrick
# Date: 09-04-2023
# Problem: Implement a algorithm to deterine if a string has all unique characters.
# Source: 1.1 from pg. 90 Cracking the Coding Interview

def isUnique(s):
  chars = {}
  for char in s:
    if char in chars:
      return False
    else:
      chars[char] = char
  return True


# Test Cases
print(isUnique("a") == True)
print(isUnique("aa") == False)
print(isUnique("abcdefg") == True)
print(isUnique("abcdefga") == False)