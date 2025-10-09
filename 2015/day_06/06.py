def iterate(part,grid,start,end,action):
    s = [int(x) for x in start.split(",")]
    e = [int(x) for x in end.split(",")]
    for y in range(s[1],e[1]+1):
        for x in range(s[0],e[0]+1):
            if part == 1:
                if action == "on":
                    grid[x][y] = True 
                elif action == "off":
                    grid[x][y] = False 
                else:
                    grid[x][y] = not grid[x][y]
            else:
                if action == "on":
                    grid[x][y] += 1 
                elif action == "off":
                    grid[x][y] = max(0,grid[x][y]-1)
                else:
                    grid[x][y] += 2

if __name__ == "__main__":

    filename = "06-input.txt"
    p1_grid = [[False] * 1000 for i in range(1000)]
    p2_grid = [[0] * 1000 for i in range(1000)]

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    for l in lines:
        tokens = l.split(" ")
        action = ""
        if tokens[0] == "turn":
            start = tokens[2]
            end = tokens[4]
            action = tokens[1]
        else:
            action = "toggle"
            start = tokens[1]
            end = tokens[3]

        iterate(1,p1_grid,start,end,action)
        iterate(2,p2_grid,start,end,action)
    print("p1: ", sum(row.count(True) for row in p1_grid))
    print("p2: ",sum(sum(row) for row in p2_grid))
