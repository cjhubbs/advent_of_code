def index_in_bounds(data,x,y):
	return x >= 0 and y >= 0 and x < len(data) and y < len(data[1])

def nearest_seat_is_occupied(data,x,y,x_inc,y_inc):
	tmp_x = x+x_inc
	tmp_y = y+y_inc		
	while 1:
		if index_in_bounds(data,tmp_x,tmp_y):
			if data[tmp_x][tmp_y] == ".":
				tmp_x += x_inc
				tmp_y += y_inc
			elif data[tmp_x][tmp_y] == "#":
				return 1
			else:
				return 0	
		else:
			return 0			

def count_neighbors(data,x,y):
	count = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if i != 0 or j != 0: #don't look at self
				count += nearest_seat_is_occupied(data,x,y,i,j)
	return count

def process_logic(data,x,y):
	neighbors = count_neighbors(data,x,y)
	space = data[x][y]
	if space == ".":
		return "."
	elif space == "L" and neighbors == 0:
		return "#"
	elif space == "#" and neighbors >= 5:
		return "L"
	else:
		return space

def iterate(data):
	new_row = []
	new_data = []	
	for y in range(len(data)):
		for x in range(len(data[0])):
				new_row.append(process_logic(data,y,x))
		new_data.append(new_row)
		new_row = []
	return new_data

f = open("input11.txt","r")
data1 = []
for l in f.read().splitlines():
	data1.append([j for j in l])
f.close()

iteration_counter = 1
next_data = iterate(data1)
while (data1 != next_data):
	data1 = next_data
	next_data = []
	next_data = iterate(data1)
	iteration_counter += 1

print(iteration_counter)
print(sum(row.count("#") for row in next_data))
