# Author: Jet Semrick
# Date: 09-05-2023
# Problem: Implement a algorithm to replace all spaces with '%20'.
# Source: 1.3 from pg. 90 Cracking the Coding Interview

def URLify(s):
  newStr = ""
  cache = ""
  for char in s:
    if char == " ":
      if len(newStr) > 0:
        cache += "%20"
    else:
      newStr += cache
      newStr += char
      cache = ""
  return newStr

# Test Cases
print(URLify("Mr John Smith     "))
print(URLify("    Mr John Smith     "))
print(URLify("MrJohnSmith"))