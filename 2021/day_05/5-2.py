from collections import namedtuple
Point = namedtuple("Point", "x y")

point_counts = {}

f = open("input5.txt", "r")

for line in f:
  ends = line.strip().split(" -> ")
  end1 = ends[0].split(",")
  end2 = ends[1].split(",")
  xs = [int(end1[0]),int(end2[0])]
  ys = [int(end1[1]),int(end2[1])]

  #process straight lines
  if xs[0] == xs[1] or ys[0] == ys[1]:
    xs.sort()
    ys.sort()
    for x in range(xs[0],xs[1]+1):
      for y in range(ys[0],ys[1]+1):
        p = Point(x,y)
        if p in point_counts:
          point_counts[p] += 1
        else:
          point_counts[p] = 1
  else:
    #process diagonal
    
    #sort so x is always ascending
    if xs[0] > xs[1]:
      xs[0],xs[1] = xs[1],xs[0]
      ys[0],ys[1] = ys[1],ys[0]

    cur_x = xs[0]
    cur_y = ys[0]
    
    while cur_x <= xs[1]:
      p = Point(cur_x,cur_y)
      if p in point_counts:
        point_counts[p] += 1
      else:
        point_counts[p] = 1
      cur_x += 1
      if ys[1] > ys[0]:
        cur_y += 1
      else:
        cur_y -= 1
                  
counter = sum(value > 1 for value in point_counts.values())
print("count is: ",counter)
