def do_math(operator, op1, op2):
  if operator == 1:
    return op1 + op2
  else:
    return op1 * op2

f = open("input-2.txt", "r")

for x in f:
  mem = list(map(int, x.split(",")))

pc = 0
mem[1] = 12
mem[2] = 2
while mem[pc] != 99:
  mem[mem[pc+3]] = do_math(mem[pc], mem[mem[pc+1]],mem[mem[pc+2]])
  pc += 4

print(mem[0])
