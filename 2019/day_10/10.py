
class Galaxy():
    def __init__(self,max):
        self.asteroids = []
        self.max = max
        
    def add(self,asteroid):
        self.asteroids.append(asteroid)

    def calc_distances(self, asteroid):
        for a in self.asteroids:
            a.r_dist = a.row - asteroid.row 
            a.c_dist = a.col - asteroid.col 
    
    def hide(self,row,col):
        for a in self.asteroids:
            if a.r_dist == row and a.c_dist == col:
                a.visible = False
                
        return
    def reset_visibility(self):
        for a in self.asteroids:
            a.visible = True

    def calc_visible(self):
        for a in self.asteroids:
            if a.r_dist != 0 or a.c_dist != 0:
                if a.r_dist == 0:
                    for b in self.asteroids:
                        if b.r_dist == 0:
                            if ((b.c_dist > a.c_dist > 0) or (b.c_dist < a.c_dist < 0)):
                                b.visible = False
                elif a.c_dist == 0:
                    for b in self.asteroids: 
                        if b.c_dist == 0:
                            if ((b.r_dist > a.r_dist > 0) or (b.r_dist < a.r_dist < 0)):
                                b.visible = False 
                elif a.c_dist == a.r_dist:
                    #diagonal
                    if a.c_dist < 0:
                        inc = -1
                    else:
                        inc = 1
                    counter = 1
                    while True:
                        offset = a.r_dist + (inc * counter)
                        if abs(offset) > self.max:
                            break 
                        self.hide(offset, offset)  
                        counter += 1
                else:
                    mult = 2
                    while True:
                        row_offset = a.r_dist * mult 
                        col_offset = a.c_dist * mult 
                        if abs(row_offset) > self.max or abs(col_offset) > self.max:
                            break 
                        self.hide(row_offset, col_offset)  
                        mult += 1
        total_visible = 0
        for a in self.asteroids:
            if a.visible:
                total_visible += 1
        return total_visible       

class Asteroid():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.r_dist = -1 
        self.c_dist = -1 
        self.visible = True
        self.num_visible = -1

if __name__ == "__main__":

    with open('10-test.txt') as f:
        lines = f.read().splitlines()
    max = len(lines)
    g = Galaxy(max)

    for index, l in enumerate(lines):
        for c in range(len(l)):
            if l[c] == '#':
                g.add(Asteroid(index,c))
    max_vis = 0
    for a in g.asteroids:
        g.calc_distances(a)
        g.reset_visibility()
        a.visible = False
        a.num_visible = g.calc_visible()
        if a.num_visible > max_vis:
            max_vis = a.num_visible 
    print("max: ",max_vis)
    for a in g.asteroids:
        print(a.row, a.col, a.num_visible)
