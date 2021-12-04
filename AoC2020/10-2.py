data = [0]
counts = [0,0]
f = open("input10-test.txt","r")
for l in f.read().splitlines():
	data.append(int(l))
	counts.append(0)	
data.sort()
data.append(data[-1]+3)
counts[0] = 1
num_of_elements = len(data)

data.append(data[-1] + 10)
data.append(data[-1] + 10)
data.append(data[-1] + 10)
data.append(data[-1] + 10)
data.append(data[-1] + 10)

for i in range(0,num_of_elements):
	if data[i+1] < data[i]+4:
		counts[i+1] += counts[i]
	if data[i+2] < data[i] + 4:
		counts[i+2] += counts[i]
	if data[i+3] < data[i] + 4:
		counts[i+3] += counts[i]
		
print(counts[-1])
