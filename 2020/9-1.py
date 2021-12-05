import itertools

pre = 25
index = pre
data = []
f = open("input9.txt","r")
for l in f.read().splitlines():
	data.append(int(l))

#part 1
while index < len(data):
	val = -1
	slice = data[index-pre:index]
	for x,y in itertools.combinations(slice,2):
		total = x+y 
		if total == data[index]:
			val = total
	#val = [x+y for x,y in itertools.combinations(slice, 2) if x+y == data[index]]
	if val == -1:
		print(str(data[index]))
		break
	index += 1

#part 2
target_sum = data[index]

starting_index = 0

while 1:
	index = starting_index
	x = data[index]
	while x < target_sum:
		index += 1
		x += data[index]
	if x == target_sum:
		print("found " + str(x) + " at range " + str(starting_index) + " to " + str(index))
		run = data[starting_index:index+1]
		run.sort()
		magic = run[0] + run[-1]
		print(run)
		print(magic)
		break
	else:
		starting_index += 1
