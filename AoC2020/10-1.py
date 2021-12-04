data = [0]
f = open("input10.txt","r")
for l in f.read().splitlines():
	data.append(int(l))

gap1count = 0
gap3count = 1
	
data.sort()
for d in range(0,len(data)):
	if d < len(data)-1: 
		if data[d+1]-data[d] == 1:
			gap1count+=1
		elif data[d+1]-data[d] == 3:
			gap3count+=1

print(gap1count)
print(gap3count)
print(gap1count*gap3count)
