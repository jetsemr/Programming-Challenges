# Author: Jet Semrick
# Date: 09-12-2023
# Problem: Implement an to detect if a string is a rotation of another.
# Source: 1.9 from pg. 91 Cracking the Coding Interview

def isRotation(s1,s2):
  if len(s1) != len(s2):
    return False
  if len(s1) == 0:
    return False
  s1s1 = s1 + s1
  return s2 in s1s1

# Test Case
print(isRotation("waterbottle", "erbottlewat") == True)
print(isRotation("watbottleer", "erbottlewat") == False)
print(isRotation("waterbottle", "erbotlewat") == False)

