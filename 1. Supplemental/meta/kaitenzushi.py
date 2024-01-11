from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten = {}
  plates = 0
  
  for d in D:
    if not d in eaten or plates - eaten[d] > K:
      eaten[d] = plates
      plates += 1

  return plates

