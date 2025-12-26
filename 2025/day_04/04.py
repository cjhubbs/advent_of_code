def count_xs(grid):
    c = 0
    for row in grid:
        c += row.count('x')
    return c

def clear_xs(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "x":
                grid[row][col] = "."

def accessible(grid,r,c):
    adj_count = -1
    max = len(grid)
    for row in range(r-1,r+2):
        for col in range(c-1,c+2):
            if 0 <= row < max and 0 <= col < max:
                if grid[row][col] == "@" or grid[row][col] == "x":
                    adj_count += 1
    return (adj_count < 4)


if __name__ == "__main__":
    filename = "04-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()

    grid = []
    for l in lines:
        grid.append(list(l))
    
    count = 0

    #p1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                if accessible(grid,row,col):
                    count += 1
    
    print(count)

    #p2
    removed = 0

    while (1):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    if accessible(grid,row,col):
                        grid[row][col] = "x"
        removable = count_xs(grid)
        if removable > 0:
            removed += removable 
            clear_xs(grid)
        else:
            print(removed)
            break 