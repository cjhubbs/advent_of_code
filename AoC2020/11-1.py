def check_pos_is_full(data,x,y):
	if x >=0 and y >= 0 and x < len(data) and y < len(data[1]):
		if data[x][y] == "#":
			return 1
		else:
			return 0
	else:
		return 0

def count_neighbors(data,x,y):
	count = 0
	for a in range(x-1,x+2):
		for b in range(y-1,y+2):
				count += check_pos_is_full(data,a,b)
	count -= check_pos_is_full(data,x,y)
	return count
		

def process_logic(data,x,y):
	neighbors = count_neighbors(data,x,y)
	space = data[x][y]
	if space == ".":
		return "."
	elif space == "L" and neighbors == 0:
		return "#"
	elif space == "#" and neighbors >= 4:
		return "L"
	else:
		return space

def iterate(data):
	global rows
	global cols
	new_row = []
	new_data = []	
	for y in range(0,rows):
		for x in range(0,cols):
				new_row.append(process_logic(data,y,x))
		new_data.append(new_row)
		new_row = []
	return new_data

def count_occupied_seats(data):
	count = 0
	for y in range(0,rows):
		for x in range(0,cols):
			if data[y][x] == "#":
				count += 1
	return count

f = open("input11.txt","r")
cols = 0
rows = 0
data1 = []
for l in f.read().splitlines():
	data1.append([j for j in l])
	cols = len(l)
	rows += 1
f.close()

iteration_counter = 1
next_data = iterate(data1)
while (data1 != next_data):
	data1 = next_data
	next_data = []
	next_data = iterate(data1)
	iteration_counter += 1

print(iteration_counter)
print(count_occupied_seats(next_data))
