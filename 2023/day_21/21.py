if __name__ == "__main__":
    with open('21-input.txt') as f:
        lines = f.read().splitlines()

    max_row = len(lines)
    max_col = len(lines[0])

    for row, l in enumerate(lines):
        if 'S' in l:
            start = [row,l.index('S')]
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    max_steps = 64
    positions = set()
    positions.add(tuple(start))
    for i in range(max_steps):
        new_positions = set()
        for p in positions:
            for d in dirs:
                new_pos = [p[0] + d[0],p[1] + d[1]]
                if 0 <= new_pos[0] < len(lines) and 0 <= new_pos[1] < len(lines[0]):
                    if lines[new_pos[0]][new_pos[1]] != '#':
                        new_positions.add(tuple(new_pos))
        positions = new_positions 

    print(len(positions))


    max_steps = 26501365
    positions = set()
    positions.add(tuple(start))
    for i in range(max_steps):
        if i % 100 == 0:
            print(i)
        new_positions = set()
        for p in positions:
            for d in dirs:
                new_pos = [p[0] + d[0],p[1] + d[1]]
                grid_row = new_pos[0] % len(lines)
                if grid_row < 0:
                    grid_row += len(lines)
                grid_col = new_pos[1] % len(lines[0])
                if grid_col < 0:
                    grid_col += len(lines[0]) 
                if lines[grid_row][grid_col] != '#':
                    new_positions.add(tuple(new_pos))
        positions = new_positions 

    print(len(positions))
