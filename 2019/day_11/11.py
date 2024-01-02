import sys
sys.path.insert(0, '../intcode')
import intcode
import itertools

f = open("11-input.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

#p1
next_dir = {"N": ['W','E'],"E": ['N','S'], "S": ['E','W'], 'W': ['S','N']}
increment = { 'N': [0,1], 'E':[1,0], 'S':[0,-1], 'W': [-1,0]}
computer = intcode.IntcodeComputer(reset_mem[:],True)
tiles = {}
pos = [0,0]
tiles[str(pos)] = 0
dir = "N"

commanded_exit = False
while not commanded_exit:
    computer.set_input(tiles[str(pos)])
    tiles[str(pos)], commanded_exit = computer.exec()
    dir_command, commanded_exit = computer.exec()
    dir = next_dir[dir][dir_command]
    pos = [pos[0] + increment[dir][0], pos[1] + increment[dir][1]]
    if not str(pos) in tiles:
        tiles[str(pos)] = 0

print("total painted tiles: ",len(tiles))