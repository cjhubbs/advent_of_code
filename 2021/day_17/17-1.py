target_x = range(14,50)
target_y = range(-267,-225)

def step(vx, vy, x, y):
  x += vx
  y += vy
  if vx > 0:
    vx -= 1
  elif vx < 0:
    vx += 1
  vy -= 1
  return vx, vy, x,y 

def in_target_zone(x,y):
  return x in target_x and y in target_y

max_y = 0
max_y_in_target = 0
pos_x = 0
pos_y = 0

for init_vy in range(1000):
  for init_vx in range(max(target_x)):
    vel_x = init_vx 
    vel_y = init_vy 
    pos_x = 0
    pos_y = 0
    
    keep_looking = 1
    while keep_looking:
      vel_x, vel_y, pos_x, pos_y = step(vel_x,vel_y, pos_x, pos_y)
      if pos_y > max_y:
        max_y = pos_y 
      if in_target_zone(pos_x, pos_y):
        keep_looking = 0
        if max_y > max_y_in_target:
          max_y_in_target = max_y
      if vel_x == 0:
        if not pos_x in target_x or pos_y < min(target_y):
          keep_looking = 0
      if pos_x > max(target_x):
        keep_looking = 0

print("max y in target was: ", max_y_in_target) 

