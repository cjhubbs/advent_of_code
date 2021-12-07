f = open("input7.txt", "r")
crabs = [int(x) for x in f.readline().strip().split(",")]

min_pos = int(min(crabs))
max_pos = int(max(crabs))

costs = [0] * (max_pos+1)
costs[1] = 1 
for i in range(2,max_pos+1):
  costs[i] = costs[i-1] + i 

least_i = -1
least_val = 10000000000

for i in range(min_pos,max_pos+1):
  total_val = 0
  distances = [abs(crab - i) for crab in crabs]
  for d in distances:
    total_val += costs[d]

  if total_val < least_val:
    least_val = total_val
    least_i = i

print("least index is: ", least_i)
print("fuel cost is: ", least_val)  
