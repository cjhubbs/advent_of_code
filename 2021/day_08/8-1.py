f = open("input8.txt", "r")
data = f.readlines()
parts = [x.strip().split("|") for x in data]

inputs = []
outputs = []
for x in parts:
  inputs.append(x[0].split())
  outputs.append(x[1].split())

count = 0
for o in outputs:
  for item in o:
    l = len(item)
    if l == 2 or l == 3 or l == 4 or l == 7:
      count += 1

print("count is:",count) 
