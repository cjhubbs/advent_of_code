import numpy 
R = 0
C = 0
def minCost(cost, m, n):
  tc = [[0 for x in range(C)] for x in range(R)]
  
  tc[0][0] = 0
  for i in range(1,m+1):
    tc[i][0] = tc[i-1][0] + cost[i][0]
  
  for j in range(1,n+1):
    tc[0][j] = tc[0][j-1] + cost[0][j]
  
  for i in range(1, m+1):
    for j in range(1,n+1):
      tc[i][j] = min(tc[i-1][j],tc[i][j-1]) + cost[i][j]
  return tc[m][n]

f = open("input15.txt", "r")
lines = f.read().splitlines()
R = len(lines)
C = len(lines[0])
grid = numpy.zeros((R,C),dtype=int)

for l in range(R):
  for d in range(C):
    grid[l][d] = int(lines[l][d])
    
  
print(minCost(grid,R-1,C-1))
