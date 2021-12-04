f = open("input13.txt","r")
data = f.read().splitlines()
start_time = int(data[0])
bus_ids = [int(d) for d in data[1].split(',') if d != "x"]
min_diff = 10000000000
bus_to_use = 0
for b in bus_ids:
	tmp = b
	while tmp < start_time:
		tmp += b
	diff = tmp - start_time
	if diff < min_diff:
		bus_to_use = b
		min_diff = diff 

print(bus_to_use)
print(min_diff)
print(bus_to_use * min_diff)
