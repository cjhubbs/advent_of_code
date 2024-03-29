import re

class Sensor():
    def __init__(self, x, y, nearest_x, nearest_y):
        self.pos = (x,y)
        self.nearest = (nearest_x, nearest_y)
        self.dist = abs(x-nearest_x) + abs(y-nearest_y)
    
    def x_extents(self):
        return [self.pos[0] - self.dist, self.pos[0] + self.dist]

    def y_extents(self):
        return [self.pos[1] - self.dist, self.pos[1] + self.dist]

    def interacts_with_target_y(self,target_y):
        extents = self.y_extents()
        return extents[0] <= target_y <= extents[1]

    def x_cov_at_y(self,target_y):
        points = set()
        y_dist = abs(self.pos[1] - target_y)
        x_dist = (self.dist - y_dist)
        x_min = self.pos[0] - x_dist 
        x_max = self.pos[0] + x_dist 
        for x in range(x_min, x_max + 1, 1):
            points.add(x)
        return points
    
    def covers_point(self,p):
        p_dist = abs(p[0] - self.pos[0]) + abs(p[1] - self.pos[1])
        return p_dist <= self.dist 

    def get_outline(self):
        points = []
        for i in range(self.dist):
            dx = i
            dy = self.dist-i+1
            points.append((self.pos[0]+dx, self.pos[1]+dy))
            points.append((self.pos[0]+dx, self.pos[1]-dy))
            points.append((self.pos[0]-dx, self.pos[1]+dy))
            points.append((self.pos[0]-dx, self.pos[1]-dy))
        return points

if __name__ == "__main__":

    sensors = []
    beacons = set()

    with open('15-input.txt') as f:
    #with open('15-input-test.txt') as f:
        lines = f.read().splitlines()
    f.close()
    for l in lines:
        coords = re.findall(r'.*=(-*\d+).+=(-*\d+).+=(-*\d+).+=(-*\d+)',l)
        sensors.append(Sensor(int(coords[0][0]),int(coords[0][1]),int(coords[0][2]),int(coords[0][3])))
        beacons.add((int(coords[0][2]),int(coords[0][3])))

    #p1
    x_coverage_at_y = set()
    target_y = 2000000
    #target_y = 20
    
    beacons_on_target_y = 0
    for b in beacons:
        if b[1] == target_y:
            beacons_on_target_y += 1

    for s in sensors:
        if s.interacts_with_target_y(target_y):
            x_coverage_at_y.update(s.x_cov_at_y(target_y))

    print(len(x_coverage_at_y) - beacons_on_target_y)

    #p2
    edges = { }
    for s in sensors:
        points = s.get_outline()
        for p in points:
            if p not in beacons:
                if p in edges.keys():
                    edges[p] += 1
                else:
                    edges[p] = 1
    for k,v in edges.items():
        if k[0] in range(target_y + 1) and k[1] in range(target_y + 1):
            covered = False
            for s in sensors:
                if s.covers_point(k):
                    covered = True
                    break
            if not covered:
                print("Uncovered point: ", k)
                print("freq = ", str(k[0]*4000000 + k[1]))
        
