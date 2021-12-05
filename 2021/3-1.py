width = 12
weight = 1
digit_count = [0]*width 
gamma = 0
epsilon = 0
line_count = 0
with open("input3.txt","r") as f:
  for line in f:
    line_count += 1
    for i in range(width):
      digit_count[i] += int(line[i])

for i in reversed(range(width)):
  if digit_count[i] > (line_count / 2):
    gamma += weight
  else:
    epsilon += weight
  weight = weight * 2

print("gamma is ")
print(gamma)
print("epsilon is ")
print(epsilon)
print(gamma*epsilon)
