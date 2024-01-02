import math 

class Asteroid():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.angle = 0
        self.dist = 0
    
    def calc_angle(self,other):
        result = math.atan2(self.row - other.row, self.col - other.col) * 180 / math.pi
        result += 90
        if result < 0:
            result += 360
        self.angle = result
        self.dist = math.sqrt((self.row - other.row)**2 + (self.col-other.col)**2)

def by_dist(ele):
    return ele.dist

if __name__ == "__main__":

    asteroids = []
    with open('10-input.txt') as f:
        lines = f.read().splitlines()

    for index, l in enumerate(lines):
        for c in range(len(l)):
            if l[c] == '#':
                asteroids.append(Asteroid(index,c))


    max_vis = 0
    max_angles = []
    host_asteroid = None
    for a in asteroids:
        angles = set()
        # calculate angle to each other asteroid
        # put angle into a set, so duplicates are eliminated
        # number of unique angles is number of visible asteroids
        for b in asteroids:
            b.calc_angle(a)
            angles.add(b.angle)
        a.num_visible = len(angles)
        
        if a.num_visible > max_vis:
            max_vis = a.num_visible
            max_angles = list(sorted(angles)) 
            host_asteroid = a

    print("max: ",max_vis)
    print("host at c,r:", host_asteroid.col, host_asteroid.row)

    asteroids_by_angle = {}
    
    #recalulate angles/distances for best host asteroid
    for b in asteroids:
        b.calc_angle(host_asteroid)

    # sort asteroids into a dictionary for quick lookup by angle
    # asteroids with the same key are kept in a list
    for a in asteroids:
        if a.angle in asteroids_by_angle:
            asteroids_by_angle[a.angle].append(a)
        else:
            asteroids_by_angle[a.angle] = [a]

    #sort the lists so the nearest at an angle comes first
    for v in asteroids_by_angle.values():
        v.sort(key=by_dist)

    # if the number of unique angles was less than the number of shots fired,
    # would need to do some mod math here. But this solution works ok.
    print(asteroids_by_angle[max_angles[199]][0].col, asteroids_by_angle[max_angles[199]][0].row)