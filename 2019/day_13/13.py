import sys
sys.path.insert(0, '../intcode')
import intcode
import itertools

f = open("13-input.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

#p1
computer = intcode.IntcodeComputer(reset_mem[:],True)

commanded_exit = False
col = 0
row = 0
tile_id = -1
block_counter = 0
while not commanded_exit:
    col, commanded_exit = computer.exec()
    row, commanded_exit = computer.exec()
    tile_id, commanded_exit = computer.exec()
    if tile_id == 2:
       block_counter += 1

print("total blocks: ", block_counter)
