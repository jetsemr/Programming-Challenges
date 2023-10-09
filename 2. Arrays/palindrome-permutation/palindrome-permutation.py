# Author: Jet Semrick
# Date: 09-07-2023
# Problem: Given a string, write a function to check if it is a permutation of a palindrome.
# Source: 1.4 from pg. 91 Cracking the Coding Interview

def palindromePermutation(s):
  chars = {}
  for char in s:
    if char not in chars:
      chars[char] = 1
    else:
      chars[char] += 1
  check = 0
  for key in chars:
    if chars[key] % 2 != 0:
      check += 1
    if check == 2:
      return False
  return True

# Test Cases
print(palindromePermutation("aba") == True)
print(palindromePermutation("abbaa") == True)
print(palindromePermutation("octopus") == False)
print(palindromePermutation("catoatc") == True)