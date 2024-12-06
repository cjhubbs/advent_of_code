import operator 

#up, right, down, left
step = [[-1,0],[0,1],[1,0],[0,-1]]
visited = {}

def log(p):
    global visited 
    visited[','.join(map(str, p))] = 1

if __name__ == "__main__":

    filename = "06-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    pos = [0,0]
    dir = 0 #up
    max = [len(lines),len(lines[0])]

    # set initial position
    for idx, l in enumerate(lines):
        if "^" in l:
            pos = [idx,l.index("^")]
            log(pos)
    
    temp = list(map(operator.add, pos, step[dir]))
    while ((0 <= temp[0] < max[0]) and (0 <= temp[1] < max[1])):
        if lines[temp[0]][temp[1]] == "#":
            dir = (dir + 1) % 4
        else:
            pos = temp
            log(pos)
        temp = list(map(operator.add, pos, step[dir]))

    print(len(visited))
        