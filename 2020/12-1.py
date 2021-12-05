ns = 0
ew = 0
heading = 90

def normalize_heading(heading):
	output = heading % 360
	if output < 0:
		output += 360
	return output

f = open("input12.txt","r")
for l in f.read().splitlines():
	command = l[0]
	value = int(l[1:len(l)])

	if command == "F":	
		if heading == 0:
			command = "N"
		elif heading == 90:
			command = "E"
		elif heading == 180:
			command = "S"
		else:
			command = "W"
		
	if command == "N":
		ns += value
	elif command == "S":
		ns -= value
	elif command == "E":
		ew += value
	elif command == "W":
		ew -= value
	elif command == "R":
		heading = normalize_heading(heading + value)
	elif command == "L":
		heading = normalize_heading(heading - value)
		
f.close()
print("ns = " + str(ns))
print("ew = " + str(ew))
print("sum = " + str (abs(ns) + abs(ew)))
