def do_math(operator, op1, op2):
  if operator == 1:
    return op1 + op2
  elif operator == 2:
    return op1 * op2

def zero_pad_left(i):
  s = str(i)
  while len(s) < 5:
    s = "0" + s
  return s

def get_input():
  return 1

f = open("input5.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

mem = reset_mem[:]
pc = 0

while mem[pc] != 99:
  print("pc = ",pc)
  if mem[pc] > 4:
    memstr = zero_pad_left(mem[pc]) 
    op = int(memstr[-2:])
    mode1 = memstr[2]
    mode2 = memstr[1]
    
    p1 = 0
    p2 = 0
    p3 = mem[pc+3]
    if mode1 == "0":
    	p1 = mem[mem[pc+1]]
    else:
    	p1 = mem[pc+1]
    if op < 3:
      if mode2 == "0":
      	p2 = mem[mem[pc+2]]
      else:
      	p2 = mem[pc+2]

  else:
    op = mem[pc]
    p1 = mem[mem[pc+1]]
    if op < 3:
      p2 = mem[mem[pc+2]]
      p3 = mem[pc+3]
      
  if op == 1:
    mem[p3] = p1+p2
    pc += 4
  elif op == 2:
    mem[p3] = p1*p2
    pc += 4
  elif op == 3:
    mem[mem[pc+1]] = get_input()
    pc += 2
  elif op == 4:
    print("op4 output = ",p1)
    pc += 2




