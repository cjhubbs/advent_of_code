target_x = range(14,50+1)
target_y = range(-267,-225+1)

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

pos_x = 0
pos_y = 0
hit_count = 0

for init_vy in range(min(target_y)-1,1000):
  for init_vx in range(max(target_x) + 1):
    vel_x = init_vx 
    vel_y = init_vy 
    pos_x = 0
    pos_y = 0
    
    keep_looking = 1
    while keep_looking:
      vel_x, vel_y, pos_x, pos_y = step(vel_x,vel_y, pos_x, pos_y)
      if in_target_zone(pos_x, pos_y):
        keep_looking = 0
        hit_count += 1
      if vel_x == 0:
        # stop if you didn't make it to x or already below y
        if not pos_x in target_x or pos_y < min(target_y):
          keep_looking = 0
      if pos_x > max(target_x):
        #stop if you're past the target
        keep_looking = 0
      if pos_y < min(target_y):
        #stop if you're below the target
        keep_looking = 0

print("hit count was: ", hit_count)
