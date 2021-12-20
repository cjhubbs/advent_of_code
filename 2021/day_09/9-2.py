import numpy

def is_lowest(arr,height,width, row,col):
  cur_is_lower = 1
  cur_val = arr[row][col]
  if row < height:
    if arr[row+1][col] <= cur_val:
      cur_is_lower = 0
  if row > 0:
    if arr[row-1][col] <= cur_val:
      cur_is_lower = 0
  if col < width:
    if arr[row][col+1] <= cur_val:
      cur_is_lower = 0
  if col > 0:
    if arr[row][col-1] <= cur_val:
      cur_is_lower = 0
  return cur_is_lower
    
def explore_basin(r,c,sea,found):
  row = r
  col = c 
  found[r][c] = 1
  if r > 0 and not found[r-1][c] and not sea[r-1][c] == 9:
    found = explore_basin(r-1,c,sea,found)
  if r < len(sea)-1 and not found[r+1][c] and not sea[r+1][c] == 9:
    found = explore_basin(r+1,c,sea,found)
  if c > 0 and not found[r][c-1] and not sea[r][c-1] == 9:
    found = explore_basin(r,c-1,sea,found)
  if c < len(sea[0])-1 and not found[r][c+1] and not sea[r][c+1] == 9:
    found = explore_basin(r,c+1,sea,found)
  return found
    
sea = []
f = open("input9.txt","r")
for line in f:
  x = []
  for c in line.strip():
    x.append(int(c))
  sea.append(x)

total_risk = 0
width = len(sea[0])
height = len(sea)
low_points = []
for r in range(height):
  for c in range(width):
    if is_lowest(sea,height-1,width-1,r,c):
      low_points.append([r,c])

basin_sizes = []
for p in low_points:
  found = numpy.zeros((height,width),dtype=int)
  found = explore_basin(p[0],p[1],sea,found)
  basin_sizes.append(numpy.count_nonzero(found))

basin_sizes.sort(reverse=True)
print(basin_sizes)
result = basin_sizes[0]*basin_sizes[1]*basin_sizes[2]
print("result is:", result)
