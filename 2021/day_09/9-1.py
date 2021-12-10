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

for r in range(height):
  for c in range(width):
    if is_lowest(sea,height-1,width-1,r,c):
      total_risk = total_risk + 1 + sea[r][c]

print("total risk is", total_risk)
