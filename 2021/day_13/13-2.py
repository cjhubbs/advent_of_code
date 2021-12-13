from collections import namedtuple
import re 
Point = namedtuple("Point", "x y")
Fold = namedtuple("Fold","axis val")
points = []
folds = []

f = open("input13.txt","r")

for line in f:
  if "," in line:
    v = line.strip().split(",")
    p = Point(int(v[0]),int(v[1]))
    points.append(p)
  if "fold along" in line:
    v = line.strip().split("=")
    f = Fold(v[0].replace("fold along ",""),int(v[1]))
    folds.append(f)

for f in folds:
  new_points = []
  for p in points:
    if f.axis == "x":
      if p.x > f.val:
        offset = (p.x-f.val)*2
        new_x = p.x - offset
      else:
        new_x = p.x 
      new_p = Point(new_x,p.y)
    else:
      if p.y > f.val:
        offset = (p.y - f.val)*2
        new_y = p.y - offset
      else:
        new_y = p.y
      new_p = Point(p.x, new_y)
    if not new_p in new_points:
      new_points.append(new_p)
  points = new_points[:]
        
grid = [[" " for i in range(40)] for j in range(6)]

for ppp in points:
  grid[int(ppp.y)][int(ppp.x)] = "#"
  
for line in grid:
  string = "".join([str(entry) for entry in line])
  print(string)

