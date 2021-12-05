from collections import namedtuple
Bus = namedtuple('Bus','id index')

f = open("input13.txt","r")
data = f.read().splitlines()
f.close()
index_count = 0
buses = []

for d in data[1].split(','):
	if d != "x":
		buses.append(Bus(int(d),index_count))
	index_count += 1

t = 0
increment = buses[0].id
num_of_buses = len(buses)
bus_to_match = 1

#Got the hint from Reddit. Once you find out where the first two line up properly,
#that alignment will recur at that period. So, you can just check every instance of
#that period until the third one lines up. Since all the bus IDs are prime, the 
#least common multiple of the IDs will just be ID * ID * ID... 
counter = 0

while bus_to_match < num_of_buses:
	counter +=1 
	t = t + increment
	if (t + buses[bus_to_match].index) % buses[bus_to_match].id == 0:
		increment *= buses[bus_to_match].id
		bus_to_match += 1

print(t)
print(counter)
