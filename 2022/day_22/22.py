import numpy as np

class jungle():
    def __init__(self, start_col,grid):
        self.pos = [0,start_col]
        self.grid = grid 
        self.dir = "R"
        self.max_dim = len(grid[0])

    def rotate(self, turn_dir):
        new_dir = {
            "R": {"L": "U", "R": "D"},
            "L": {"L": "D", "R": "U"},
            "U": {"L": "L", "R": "R"},
            "D": {"L": "R", "R": "L"}
        }

        self.dir = new_dir[self.dir][turn_dir]
    
    def move(self, dist):
        steps = { "R": [0,1],
                  "L": [0,-1],
                  "U": [-1,0],
                  "D": [1,0] }
        step = steps[self.dir]
        for i in range(dist):
            new_row = (self.pos[0] + step[0]) % self.max_dim
            new_col = (self.pos[1] + step[1]) % self.max_dim 
            if self.grid[new_row][new_col] == ".":
                self.pos = [new_row, new_col]
            elif self.grid[new_row][new_col] == "#":
                pass #pos doesn't change
            else:
                while self.grid[new_row][new_col] == " ":
                    new_row = (new_row + step[0]) % self.max_dim
                    new_col = (new_col + step[1]) % self.max_dim
                if self.grid[new_row][new_col] == ".":
                    self.pos = [new_row, new_col]
    
    def get_score(self):
        facing_points = { "R": 0, "D": 1, "L": 2, "U":3}
        return (1000*(self.pos[0]+1) + 4*(self.pos[1]+1) + facing_points[self.dir])
            
if __name__ == "__main__":

    with open('22-input.txt') as f:
        lines = f.read().splitlines()
    f.close()
    map = []
    moves = ""
    longest_map = 0
    start_col = -1
    for l in lines:
        if "." in l:
            if start_col == -1:
                start_col = l.index(".")
            map.append(l)
            if len(l) > longest_map:
                longest_map = len(l)
        elif "L" in l:
            moves = l
    max_dim = longest_map if longest_map > len(map) else len(map)

    grid = np.full((max_dim, max_dim)," ")
    for row in range(len(map)):
        for col in range(len(map[row])):
            grid[row][col] = map[row][col]
    
    j = jungle(start_col,grid)

    num_str = ""
    for c in moves:
        if c.isnumeric():
            num_str += c 
        else:
            dist = int(num_str)
            num_str = ""
            j.move(dist)
            j.rotate(c)
    dist = int(num_str)
    j.move(dist)
    print(j.get_score())
