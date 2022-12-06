def find_key(line, keylen):
  for i in range(len(line)):
    sl = line[i:i+keylen]
    se = set(list(sl))
    if len(se) == keylen:
      return(str(i+keylen)) 

with open('6-input.txt') as f:
  line = f.readline()

p1 = find_key(line,4)
p2 = find_key(line,14)

print("P1, P2 = ", p1, ", ", p2)

