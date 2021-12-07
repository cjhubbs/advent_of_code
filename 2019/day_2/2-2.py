def do_math(operator, op1, op2):
  if operator == 1:
    return op1 + op2
  else:
    return op1 * op2

f = open("input-2.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

mem = reset_mem[:]
pc = 0

for noun in range(99):
  for verb in range(99):
    mem[1] = noun
    mem[2] = verb
    while mem[pc] != 99:
      mem[mem[pc+3]] = do_math(mem[pc], mem[mem[pc+1]],mem[mem[pc+2]])
      pc += 4
    if mem[0] == 19690720:
      print("noun is " + str(noun))
      print('verb is ' + str(verb))
      ans = noun*100 +verb
      print(ans)
    mem = reset_mem[:]
    pc = 0

