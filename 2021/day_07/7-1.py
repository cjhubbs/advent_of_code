f = open("input7.txt", "r")
crabs = [int(x) for x in f.readline().strip().split(",")]

min = min(crabs)
max = max(crabs)

least_i = -1
least_val = 1000000

for i in range(min,max+1):
  distances = [abs(crab - i) for crab in crabs]
  total_val = sum(distances)
  if total_val < least_val:
    least_val = total_val
    least_i = i

print("least index is: ", least_i)
print("fuel cost is: ", least_val)  
