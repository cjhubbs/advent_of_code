import math 

def fuel_required(mass):
	return (math.floor(int(mass)/3) - 2)

f = open("input-1.txt", "r")
total_mass = 0
total_part_2 = 0
temp_fuel = 0

for x in f:
  total_mass += fuel_required(x)
  temp_fuel = fuel_required(x)
  
  while temp_fuel > 0:
  	total_part_2 += temp_fuel
  	temp_fuel = fuel_required(temp_fuel)

print(total_mass)
print(total_part_2)
