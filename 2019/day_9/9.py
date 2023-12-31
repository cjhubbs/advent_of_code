import sys
sys.path.insert(0, '../intcode')
import intcode
import itertools

f = open("9-input.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

#p1
computer = intcode.IntcodeComputer(reset_mem[:])
computer.set_input(1)
print(computer.exec())

#p2
computer = intcode.IntcodeComputer(reset_mem[:])
computer.set_input(2)
print(computer.exec())
