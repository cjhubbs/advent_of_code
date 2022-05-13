import numpy as np
import heapq 

def astar_solve(data, max_l):
  start_node = (0,0)
  end_node = (max_l -1, max_l - 1)
  
  open_queue = []
  closed_queue = set()
  parents = { }
  g_score = {}

  for y in range(len(data)):
    for x in range(len(data)):
      g_score[(y,x)] = np.Inf
      
  g_score[start_node]= 0
  heapq.heappush(open_queue,(get_cityblock(start_node,end_node),start_node))
  
  while open_queue:
    _, node = heapq.heappop(open_queue)
    if node == end_node:
      total = 0
      while node in parents:
        x = node[0]
        y = node[1]
        total += data[y][x]
        node = parents[node]
      return total 
    elif node in closed_queue:
      continue
    else:
      neighbors = get_neighbors(data, node)
      for n in neighbors:
        if n in closed_queue:
          continue
        x = n[0]
        y = n[1]
        added_g_score = data[y][x]
        candidate_g = g_score[node] + added_g_score
        if candidate_g <= g_score[n]:
          g_score[n] = candidate_g
          parents[n] = node 
          f = get_cityblock(n, end_node) + candidate_g
          heapq.heappush(open_queue,(f,n))
      closed_queue.add(node)

def get_cityblock(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(data, node):
  x = node[0]
  y = node[1]
  node_neighbors = []
  neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
  for i in neighbors:
    if (0 <= i[0] <= ROWS*5 - 1) and (0 <= i[1] <= ROWS*5 -1):
      node_neighbors.append(i)
  return node_neighbors
          

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

cost = astar_solve(grid,ROWS*5)
print ("cost is: ",cost)

