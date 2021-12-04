f = open("input5.txt", "r")
max_id = 0
found_ids = []

for x in f: 
	min_row = 0
	max_row = 127
	min_seat = 0
	max_seat = 7
	row_increment = 64
	seat_increment = 4
	
	for i in range(7):
		if x[i] == "F":
			max_row -= row_increment
		else:
			min_row += row_increment
		row_increment /= 2			
	
	for i in range(3):
		if x[i+7] == "L":
			max_seat -= seat_increment
		else:
			min_seat =+ seat_increment
		seat_increment /= 2
	
	unique_id = (max_row * 8) + max_seat
	found_ids.append(int(unique_id))

	if unique_id > max_id:
		max_id = unique_id

print("highest unique id: " + str(max_id))
found_ids.sort()
for y in range(len(found_ids)):
	if y>0:
		if found_ids[y-1]!=found_ids[y]-1:
			print("ids: " + str(found_ids[y-1]) + ", " + str(found_ids[y]) + ", " +str(found_ids[y+1]))
