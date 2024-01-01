import math 

class Asteroid():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.angle = 0
    
    def calc_angle(self,other):
        result = math.atan2(self.row - other.row, self.col - other.col) * 180 / math.pi
        if result < 0:
            result += 360
        self.angle = result

if __name__ == "__main__":

    asteroids = []
    with open('10-input.txt') as f:
        lines = f.read().splitlines()

    for index, l in enumerate(lines):
        for c in range(len(l)):
            if l[c] == '#':
                asteroids.append(Asteroid(index,c))


    max_vis = 0
    for a in asteroids:
        angles = set()
        for b in asteroids:
            b.calc_angle(a)
            angles.add(b.angle)
        a.num_visible = len(angles)
        
        if a.num_visible > max_vis:
            max_vis = a.num_visible 
    print("max: ",max_vis)
