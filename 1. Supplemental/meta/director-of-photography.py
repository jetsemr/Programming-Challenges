# Author: Jet Semrick
# Date: 11-8-2023
# Problem: Count the number of photos.
# Source: Meta Careers

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  photos = 0
  start = next((i for i in range(N) if C[i] in ['P', 'B']), N)
  for i in range(start, N):
    if C[i] == "A":
      left = C[max(0,i-Y):max(0,i-X+1)]
      right = C[min(i+X, N):min(i+Y+1,N)]
      pabs = sum(1 for p in left if p == 'P') * sum(1 for b in right if b == 'B') 
      baps = sum(1 for b in left if b == 'B') * sum(1 for p in right if p == 'P')
      photos += pabs + baps
  return photos 
