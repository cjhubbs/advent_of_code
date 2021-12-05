from collections import namedtuple
Coords = namedtuple('Coords','ns ew')

ns = 0
ew = 0
waypoint_ns = 1
waypoint_ew = 10


def rotate_waypoint(value,input_coords):
	new_ns = 0
	new_ew = 0
	
	if value == 90 or value == -270:
		new_ew = input_coords.ns
		new_ns = -input_coords.ew
	if value == 180 or value == -180:
		new_ns = -input_coords.ns
		new_ew = -input_coords.ew
	if value == 270 or value == -90:
		new_ew = -input_coords.ns
		new_ns = input_coords.ew
	output_coords = Coords(new_ns, new_ew)
	return output_coords

f = open("input12.txt","r")
for l in f.read().splitlines():
	command = l[0]
	value = int(l[1:len(l)])

	if command == "F":
		ns += value*waypoint_ns
		ew += value*waypoint_ew	
	elif command == "N":
		waypoint_ns += value
	elif command == "S":
		waypoint_ns -= value
	elif command == "E":
		waypoint_ew += value
	elif command == "W":
		waypoint_ew -= value
	elif command == "R":
		current_coords = Coords(waypoint_ns, waypoint_ew)
		new_coords = rotate_waypoint(value,current_coords)
		waypoint_ns = new_coords.ns
		waypoint_ew = new_coords.ew
	elif command == "L":
		current_coords = Coords(waypoint_ns, waypoint_ew)
		new_coords = rotate_waypoint(-value,current_coords)
		waypoint_ns = new_coords.ns
		waypoint_ew = new_coords.ew		
f.close()
print("ns = " + str(ns))
print("ew = " + str(ew))
print("sum = " + str (abs(ns) + abs(ew)))
