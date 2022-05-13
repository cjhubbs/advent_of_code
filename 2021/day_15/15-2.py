import numpy as np
from collections import namedtuple
from heapq import heappop,heappush  
import sys 

Node = namedtuple("Node", "x y")
Path = namedtuple("Path", "cost node")

ROWS = 0
COLS = 0

def find_path(map, start, goal):
  max_y = len(map) - 1
  max_x = len(map[0]) - 1
  
  start_risk = map[start.y, start.x]
  
  not_visited:list[Path] = [Path(start_risk, start)]
  visited:list[Node] = []
  
  while not_visited:
    risk, node = heappop(not_visited)
    if node == goal: return risk - start_risk
    if node in visited: continue
    x,y = node 
    
    choices = (x+1, y),(x-1,y),(x,y+1),(x,y-1)
    for next_x, next_y in choices:
      if (x <= next_x <= max_x) and (0 <= next_y <= max_y):
        next_risk = risk + map[next_y][next_x]
        next_node = Node(next_x, next_y)
        heappush(not_visited, Path(next_risk, next_node))
    visited += [node]

def minCost(cost, m, n):
  tc = [[0 for x in range(COLS*5)] for x in range(ROWS*5)]
  
  tc[0][0] = 0
  for i in range(1,m+1):
    tc[i][0] = tc[i-1][0] + cost[i][0]
  
  for j in range(1,n+1):
    tc[0][j] = tc[0][j-1] + cost[0][j]
  
  for i in range(1, m+1):
    for j in range(1,n+1):
      tc[i][j] = min(tc[i-1][j],tc[i][j-1]) + cost[i][j]
  return tc[m][n]

np.set_printoptions(threshold=sys.maxsize)
f = open("input15.txt", "r")
lines = f.read().splitlines()
ROWS = len(lines)
COLS = len(lines[0])
print("ROWS = ",ROWS)
print("COLS = ", COLS)
grid = np.zeros((ROWS*5,COLS*5),dtype=int)

for r in range(ROWS):
  for c in range(COLS):
    grid[r][c] = int(lines[r][c])
    inc_cost = grid[r][c]
    for i in range(1,5):
      inc_cost = inc_cost+1
      if inc_cost == 10:
        inc_cost = 1
      grid[r][c+(COLS*i)] = inc_cost
      
for r in range(ROWS*4):
  temp_row = grid[r][COLS:]
  temp_end = temp_row[-COLS:]
  for n in temp_end:
    t = n + 1    
    if t == 10:
      t = 1      
    temp_row = np.append(temp_row,t)
  grid[r+ROWS] = temp_row

grid[0][0] = 0
cost = find_path(grid,Node(0,0), Node(ROWS*5-1,COLS*5-1))
print ("cost is: ",cost)
#print(minCost(grid,ROWS*5-1,COLS*5-1))
