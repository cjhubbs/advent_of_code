import sys
sys.path.insert(0, '../intcode')
import intcode
import itertools

f = open("7-input.txt", "r")

for x in f:
  reset_mem = list(map(int, x.split(",")))

possible_inputs = list(itertools.permutations([0,1,2,3,4]))
max_input = 0
for inp in possible_inputs:
    num_of_amps = 5
    amplifiers = []
    for i in range(num_of_amps):
        amplifiers.append(intcode.IntcodeComputer(reset_mem[:]))
    inputs = inp
    input2 = 0
    for i in range(num_of_amps):
        amplifiers[i].set_input(inputs[i])
        amplifiers[i].set_input(input2)
        input2, done = amplifiers[i].exec()
    if input2 > max_input:
        max_input = input2 
print ("p1 max possible: ",max_input)

#p2
possible_inputs = list(itertools.permutations([5,6,7,8,9]))
max_input = 0
for inp in possible_inputs:
    num_of_amps = 5
    amplifiers = []
    for i in range(num_of_amps):
        amplifiers.append(intcode.IntcodeComputer(reset_mem[:]))
    inputs = inp
    input2 = 0

    for i in range(num_of_amps):
        amplifiers[i].set_input(inputs[i])

    done = False
    final_val = 0
    while not done:
        for i in range(num_of_amps):
            amplifiers[i].set_input(input2)
            input2, done = amplifiers[i].exec()
            if not done:
                final_val = input2

    if final_val > max_input:
        max_input = final_val 
print ("p2 max possible: ",max_input)
