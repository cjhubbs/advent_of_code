from collections import namedtuple
Point = namedtuple("Point", "x y")

wire_points = [[],[]]

cur_x = 0
cur_y = 0
cur_wire = 0

f = open("input3.txt", "r")

for line in f:
  commands = line.strip().split(",")
  
  for c in commands:
    dir = c[0]
    val = int(c[1:])
    if dir == "R":
      for i in range(val):
        cur_x += 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
    if dir == "L":
      for i in range(val):
        cur_x -= 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
    if dir == "U":
      for i in range(val):
        cur_y += 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
    if dir == "D":
      for i in range(val):
        cur_y -= 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
          
  cur_wire += 1
  cur_x = 0
  cur_y = 0

found = set(wire_points[0]).intersection(wire_points[1])

min_distance = 10000
for f in found:
  dist = abs(f[0])+abs(f[1])
  if dist < min_distance: min_distance = dist 
     
print(min_distance)
