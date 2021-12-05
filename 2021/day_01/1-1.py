f = open("input1.txt","r")
data = f.read().splitlines()
f.close()

prev_val = -1

inc_count = -1
for d in data:
  if int(d) > prev_val:
    inc_count += 1
  prev_val = int(d)

print(inc_count)
