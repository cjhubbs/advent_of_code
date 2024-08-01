import numpy 

grid_sn = 8868
grid = numpy.zeros((301,301),dtype=int)
total_power = numpy.zeros((301,301),dtype=int)
tp3d = numpy.zeros((301,301,301),dtype=int)

for x in range(1,301):
    for y in range(1,301):
        rack_id = x+10
        power_level = rack_id * y
        power_level += grid_sn 
        power_level *= rack_id 
        if power_level < 100:
            grid[x][y] = -5
        else:
            hunds_char = str(power_level)[-3]
            grid[x][y] = int(hunds_char) - 5

#p1
for x in range(1,298):
    for y in range(1,298):
        total_power[x][y] = numpy.sum(grid[x:x+3,y:y+3])

idx = numpy.unravel_index(numpy.argmax(total_power),total_power.shape)
print(idx)

#p2
for z in range(1,301):
    for x in range(1,301-z):
        for y in range(1,301-z):
            tp3d[x][y][z] = numpy.sum(grid[x:x+z,y:y+z])

idx = numpy.unravel_index(numpy.argmax(tp3d),tp3d.shape)
print(idx)
