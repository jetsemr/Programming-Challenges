## 7-19-2022
## Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
from math import pi

def radians_to_degrees(radians):
  return radians * (180/pi)

# Test 1
if (round(radians_to_degrees(1),1) == 57.3):
  print("Test 1: PASS")
else:
  print("Test 1: FAIL")

# Test 2
if (round(radians_to_degrees(20),1) == 1145.9):
  print("Test 2: PASS")
else:
  print("Test 2: FAIL")

# Test 3
if (round(radians_to_degrees(50),1) == 2864.8):
  print("Test 3: PASS")
else:
  print("Test 3: FAIL")
