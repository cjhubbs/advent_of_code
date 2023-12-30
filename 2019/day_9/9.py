import sys
sys.path.insert(0, '../intcode')
import intcode
import itertools

f = open("9-input.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))
computer = intcode.IntcodeComputer(reset_mem[:])
computer.set_input(1)
print(computer.exec()[0])