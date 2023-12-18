import numpy as np 

start = [0,0]
cur = [0,0]
prev = [-1,-1]

move_offset = {
    'N': [-1,0],
    'S': [1,0],
    'E': [0,1],
    'W': [0,-1]
}

valid_moves = {
    'N': '|F7S',
    'S': '|LJS',
    'E': '-J7S',
    'W': '-LFS'
}

offsets = {
    "|": [[-1,0],[1,0]],
    "-": [[0,-1],[0,1]],
    "L": [[-1,0],[0,1]],
    "J": [[-1,0],[0,-1]],
    "7": [[1,0],[0,-1]],
    "F": [[1,0],[0,1]]
}

dirs = 'NSEW'

if __name__ == "__main__":
    with open('10-input.txt') as f:
        lines = f.read().splitlines()
    row_counter = 0
    lines.insert(0,'.'* len(lines[0]))
    lines.append('.'*len(lines[0]))
    for index, l in enumerate(lines):
        lines[index] = '.' + l + '.'
        if 'S' in l:
            start = [row_counter,l.index('S')+1]
        row_counter += 1

    print(start[0],start[1])
    cur = start 
    step_counter = 0
    for m in valid_moves:
        possible_pos = [cur[0] + move_offset[m][0],cur[1] + move_offset[m][1]]
        if possible_pos != prev and lines[possible_pos[0]][possible_pos[1]] in valid_moves[m]:
            prev = cur 
            cur = possible_pos
            step_counter += 1
            break 

    while True:
        possible_offsets = offsets[lines[cur[0]][cur[1]]]
        if np.array_equal(np.add(cur, possible_offsets[0]), prev):
            prev = cur
            cur = np.add(cur, possible_offsets[1])     
        else:
            prev = cur 
            cur = np.add(cur, possible_offsets[0])
        step_counter += 1            
        if np.array_equal(cur,start) and prev[0] != -1:
            break
    print(step_counter / 2)
