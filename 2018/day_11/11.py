import numpy 

grid_sn = 8868
grid = numpy.zeros((301,301),dtype=int)
total_power = numpy.zeros((301,301),dtype=int)

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

for x in range(1,298):
    for y in range(1,298):
        total_power[x][y] = numpy.sum(grid[x:x+3,y:y+3])

idx = numpy.unravel_index(numpy.argmax(total_power),total_power.shape)
print(idx)
