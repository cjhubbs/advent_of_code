beams = []
beam_complete = []
dir_offset = {'U': [-1,0],'D': [1,0],'L': [0,-1],'R': [0,1]}
forward_mirror_change = {'U': 'R','D':'L','R':'U','L':'D'}
backward_mirror_change = {'U': 'L','D':'R','R':'D','L':'U'}

class Beam():
    def __init__(self,row, col, dir):
        self.col = col 
        self.row = row 
        self.dir = dir
    def pos_string(self):
        return ','.join([str(self.row),str(self.col)])
    def vec_string(self):
        return ','.join([str(self.row), str(self.col), self.dir])

    def move(self,grid):
        if grid[self.row][self.col] ==  '/':
            self.dir = forward_mirror_change[self.dir]
        if grid[self.row][self.col] ==  '\\':
            self.dir = backward_mirror_change[self.dir]
        if grid[self.row][self.col] ==  '|':
            if self.dir in ['L','R']:
                self.dir = 'U'
                beams.append(Beam(self.row, self.col,'D'))
                beam_complete.append(False)
        if grid[self.row][self.col] ==  '-':
            if self.dir in ['U','D']:
                self.dir = 'L'
                beams.append(Beam(self.row, self.col,'R'))
                beam_complete.append(False)
        
        self.row += dir_offset[self.dir][0]
        self.col += dir_offset[self.dir][1]
        if 0 <= self.row < len(grid) and 0 <= self.col < len(grid[0]):
            return [str(self.row),str(self.col),self.dir]
        else:
            return "off"

def run_grid(start_row, start_col, start_dir,grid):
    global beams
    global beam_complete 
    beams = []
    beam_complete = []
    points = set()
    hits = set()

    beams.append(Beam(start_row,start_col,start_dir))
    beam_complete.append(False)
    points.add(beams[0].pos_string())
    hits.add(beams[0].vec_string())

    while True:
        if all(c == True for c in beam_complete):
            break 
        for i in range(len(beams)):
            if not beam_complete[i]:
                new_vector = beams[i].move(lines)
                if new_vector == 'off':
                    beam_complete[i] = True
                else:
                    new_pos = ','.join([new_vector[0],new_vector[1]])
                    new_vec = ','.join(new_vector)
                    if new_vec in hits:
                        beam_complete[i] = True 
                    else:
                        hits.add(new_vec)
                        points.add(new_pos)
    return len(points)    

if __name__ == "__main__":
    with open('16-input.txt') as f:
      lines = f.read().splitlines()

    print("p1 total cells activated: ",run_grid(0,0,'R',lines))
    
    max_hits = 0
    for r in range(len(lines)):
        res = run_grid(r,0,'R',lines)
        max_hits = max(res,max_hits)
        res = run_grid(r,len(lines[0])-1,'L',lines)
        max_hits = max(res,max_hits)
    for c in range(len(lines[0])):
        res = run_grid(0,c,'D',lines)
        max_hits = max(res,max_hits)
        res = run_grid(len(lines)-1,c,'U',lines)
        max_hits = max(res,max_hits)
    print("p2 max total cells activated: ",max_hits)