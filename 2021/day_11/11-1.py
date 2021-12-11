octopi = []
num_of_steps = 5000
dimension = 10
flashed_this_step = [[0*dimension]*dimension]

def execute_flash(i,j):
  if not flashed_this_step[i][j]:
    flashed_this_step[i][j] = 1
    for x in range(i-1,i+2):
      for y in range(j-1,j+2):
        if x != i or y != j:
          if x in range(dimension) and y in range(dimension):
            octopi[x][y] += 1
            if (octopi[x][y] > 9):
              execute_flash(x,y)              

def step():
  #increment every octopus by 1
  for i in range(dimension):
    for j in range(dimension):
      octopi[i][j] += 1
      flashed_this_step[i][j] = 0
       
  for i in range(dimension):
    for j in range(dimension):
      if octopi[i][j] > 9:
        execute_flash(i, j)   
  for i in range(dimension):
    for j in range(dimension):
      if octopi[i][j] > 9:
        octopi[i][j] = 0
  return sum([i.count(1) for i in flashed_this_step])    

f = open("input11.txt","r")
for line in f.readlines():
  l = []
  f = []
  for c in line.strip():
    l.append(int(c))
    f.append(0)
  octopi.append(l)
  flashed_this_step.append(f)

flash_count = 0
for i in range(num_of_steps):
  flashes_this_cycle = step()
  flash_count += flashes_this_cycle
  
  if i == 99:
    print("Flash count at 100 steps is:",flash_count)    
  
  o_sum = sum(sum(octopi,[]))
  if o_sum == 0:
    print("simultaneous flash at step ", i+1)
    break
  

