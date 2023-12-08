import re 
from math import lcm

steps = ""
big_map = {}
starts = []

if __name__ == "__main__":
    with open('08-input.txt') as f:
        lines = f.read().splitlines()
    steps = lines[0]
    del lines[0]
    del lines[0]
    
    for l in lines:
        result = re.search("(.{3}) = \((.{3}), (.{3})\)",l)
        big_map[result.group(1)] = {'L': result.group(2),'R': result.group(3)}
        if result.group(1)[2] == 'A':
            starts.append(result.group(1))

    #p1
    next = 'AAA'
    i = 0
    step_counter = 0
    while next != 'ZZZ':
        next = big_map[next][steps[i]]
        i = (i+1) % len(steps)
        step_counter+=1
    print('p1 steps: ',step_counter)

    #p2
    i = 0
    step_counter = 0
    hits = {}
    while True:
        step_counter+=1
        for j in range(len(starts)):
            starts[j] = big_map[starts[j]][steps[i]]
            if starts[j][2] == "Z":
                if not j in hits:
                    hits[j] = step_counter
        i = (i+1) % len(steps)
        if len(hits) == len(starts):
            break 
    print('p2 steps: ',lcm(hits[0],hits[1],hits[2],hits[3],hits[4],hits[5]))
    
