def iterate(d):
  new_d = [["." for i in range(len(d[0]))] for j in range(len(d))]
  
  for r in range(len(d)):
    new_r = (r+1) % len(d)
    for c in range(len(d[0])):
      new_c = (c+1) % len(d[0])
      if d[r][c] == '>':
        if d[r][new_c] == '.':
          new_d[r][new_c] = '>'
          new_d[r][c] = '.'
        else:
          new_d[r][c] = '>'

  for r in range(len(d)):
    new_r = (r+1) % len(d)
    for c in range(len(d[0])):
      new_c = (c+1) % len(d[0])
      if d[r][c] == 'v':
        if d[new_r][c] == 'v' or new_d[new_r][c] == ">":
          #stuck
          new_d[r][c] = 'v'
        else:
          new_d[new_r][c] = 'v'
         
  return new_d

data = []
f = open("input25.txt", "r")
lines = f.read().splitlines()
for l in lines:
  data.append(list(l))

newdata = []
exit = 0
counter = 0
print("Data:")
print(data)
while exit == 0:
  counter += 1
  newdata = iterate(data)
  match = True
  for r in range(len(newdata)):
    for c in range(len(newdata[0])):
      match = match and data[r][c] == newdata[r][c]
      if match == False:
        break
    if match == False:
      break

  if match:
    exit = 1
  else:
    data = newdata

print(counter)
