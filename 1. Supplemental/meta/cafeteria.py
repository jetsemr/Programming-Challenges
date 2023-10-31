# Date: 11-1-2023
# Author: Jet Semrick
# Problem: Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
# Source: Cateria problem from Meta interview prep

import math

# N = number of seats, K = social distance, M = number of current diners, S = position of current diners
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  
  # sort the list of filled seats
  S.sort()
  start, result = 1,0
 
  # attach a "termination" seat
  S.append(N+K+1)
  
  # iterate through filled seats
  for s in S:
    # see if new seat is possible
    delta = s - K - start
    if delta > 0:
      # add a new seat
      result += math.ceil(delta / (K+1))
    # find next potential start
    start = s+K+1
  return result
  
