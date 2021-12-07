from collections import namedtuple
Point = namedtuple("Point", "x y")

wire_points = [[],[]]
step_counts = [{},{}]

cur_x = 0
cur_y = 0
cur_wire = 0

f = open("input3.txt", "r")

for line in f:
  commands = line.strip().split(",")
  step_counter = 0
  
  for c in commands:
    dir = c[0]
    val = int(c[1:])
    if dir == "R":
      for i in range(val):
        cur_x += 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
        if not p in step_counts[cur_wire].keys():
          step_counts[cur_wire][p] = step_counter
        step_counter += 1
    if dir == "L":
      for i in range(val):
        cur_x -= 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
        if not p in step_counts[cur_wire].keys():
          step_counts[cur_wire][p] = step_counter
        step_counter += 1
    if dir == "U":
      for i in range(val):
        cur_y += 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
        if not p in step_counts[cur_wire].keys():
          step_counts[cur_wire][p] = step_counter
        step_counter += 1
    if dir == "D":
      for i in range(val):
        cur_y -= 1
        p = Point(cur_x,cur_y)
        wire_points[cur_wire].append(p)
        if not p in step_counts[cur_wire].keys():
          step_counts[cur_wire][p] = step_counter
        step_counter += 1
    
          
  cur_wire += 1
  cur_x = 0
  cur_y = 0

found = set(wire_points[0]).intersection(wire_points[1])

min_distance = 10000
for f in found:
  dist = step_counts[0][f] + step_counts[1][f] + 2
  if dist < min_distance: min_distance = dist 
     
print(min_distance)
