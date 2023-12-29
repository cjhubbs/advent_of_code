import intcode

f = open("input5.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

mem = reset_mem[:]
pc = 0

#p1
p1_computer = intcode.IntcodeComputer(reset_mem[:])
p1_computer.set_input(1)
p1_computer.exec()

#p2
p2_computer = intcode.IntcodeComputer(reset_mem[:])
p2_computer.set_input(5)
p2_computer.exec()

