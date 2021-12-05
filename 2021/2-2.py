h_pos = 0
depth = 0
aim = 0

with open("input2.txt","r") as f:
  for line in f:
    data = line.split(" ")
    if data[0] == "forward":
      h_pos += int(data[1])
      depth += (int(data[1])*aim)
    elif data[0] == "down":
      aim += int(data[1])
    elif data[0] == "up":
      aim -= int(data[1])
      
print(h_pos)
print(depth)
print(h_pos*depth)
