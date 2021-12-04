circle = [3,2,7,4,6,5,1,8,9]

def find_index_for_value(c,val):
	for i in range(len(c)):
		if c[i] == val:
			return i
	return -1

def max_val_in_circle(c):
	max = -1
	for v in c:
		if v > max:
			max = v 
	return max 

current = 0
sublist = []

for i in range(100):
	sublist = []
	next_index = (current+1)%len(circle)
	val_of_current = circle[current]
	
	#extract 3 cups
	for j in range(3):
		sublist.append(circle.pop(next_index))
		if next_index > len(circle)-1:
			next_index = 0
	
	search_target = val_of_current-1
	ind = find_index_for_value(circle,search_target)
	while ind == -1:
		search_target -= 1
		if search_target < 1:
			search_target = max_val_in_circle(circle)
		ind = find_index_for_value(circle,search_target)
	
	circle.insert(ind+1,sublist.pop(0))
	circle.insert(ind+2,sublist.pop(0))
	circle.insert(ind+3,sublist.pop(0))
	
	new_index_of_current = find_index_for_value(circle,val_of_current)
	current = (new_index_of_current+1)%len(circle)
	
final_str = ""
ind = (find_index_for_value(circle,1)+1)%len(circle)
while ind < len(circle):
	final_str += str(circle.pop(ind))
while(circle):
	final_str += str(circle.pop(0))
print(final_str)
	
