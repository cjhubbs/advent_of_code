import sys
sys.path.insert(0, '../intcode')
import intcode

f = open("input5.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

#reset_mem = [3,0,4,0,99]

mem = reset_mem[:]
pc = 0

#p1
p1_computer = intcode.IntcodeComputer(reset_mem[:])
p1_computer.set_input(1)
print(p1_computer.exec())

#p2
p2_computer = intcode.IntcodeComputer(reset_mem[:])
p2_computer.set_input(5)
print(p2_computer.exec())

