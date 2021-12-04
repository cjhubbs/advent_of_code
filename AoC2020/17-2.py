import numpy as np
limit = 30 

def check_pos(g,x,y,z,w):
	if x < 0 or y < 0 or z < 0 or w < 0 or x > limit-1 or y>limit-1 or z>limit-1 or w>limit-1:
		return 0
	else:
		return g[x][y][z][w]

def num_of_active_neighbors(g,x,y,z,w):
	count = 0
	for tmp_x in range(x-1,x+2):
		for tmp_y in range(y-1,y+2):
			for tmp_z in range(z-1,z+2):
				for tmp_w in range(w-1,w+2):
					if tmp_x != x or tmp_y != y or tmp_z != z or tmp_w != w:
						count += check_pos(g,tmp_x,tmp_y,tmp_z,tmp_w)
	return count

def cycle_galaxy(g):
	new_gal = np.zeros((limit,limit,limit,limit),dtype=int)	
	for gal_x in range(limit):
		for gal_y in range(limit):
			for gal_z in range(limit):
				for gal_w in range(limit):
					neighbors = num_of_active_neighbors(g,gal_x,gal_y,gal_z,gal_w)
					if g[gal_x][gal_y][gal_z][gal_w] == 1:
						if neighbors == 2 or neighbors == 3:
							new_gal[gal_x][gal_y][gal_z][gal_w] = 1
					else:
						if neighbors == 3:
							new_gal[gal_x][gal_y][gal_z][gal_w] = 1
	return new_gal

offset = 10
galaxy = np.zeros((limit,limit,limit,limit),dtype=int)

f = open("input17.txt","r")
data = f.read().splitlines()
f.close()
x = offset
y = offset
z = offset
w = offset
for d in data:
	for c in range(len(d)):
		if d[c] == "#":
			galaxy[c + offset][y][z][w] = 1
	y += 1


galaxy1 = cycle_galaxy(galaxy)
galaxy2 = cycle_galaxy(galaxy1)
galaxy3 = cycle_galaxy(galaxy2)
galaxy4 = cycle_galaxy(galaxy3)
galaxy5 = cycle_galaxy(galaxy4)
galaxy6 = cycle_galaxy(galaxy5)

result = np.sum(galaxy6)
print(result)
