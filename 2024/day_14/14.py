import re 

x_max = 101
y_max = 103
cycles = 100

def count_quadrants(robots):
    quad_x = [[0,int((x_max-3)/2)],[int((x_max+1)/2),x_max-1]]
    quad_y = [[0,int((y_max-3)/2)],[int((y_max+1)/2),y_max-1]]
    counts = [0,0,0,0]
    for r in robots:
        if   quad_x[0][0] <= r.x <= quad_x[0][1] and quad_y[0][0] <= r.y <= quad_y[0][1]:
            counts[0] += 1
        elif quad_x[1][0] <= r.x <= quad_x[1][1] and quad_y[0][0] <= r.y <= quad_y[0][1]:
            counts[1] += 1
        elif quad_x[0][0] <= r.x <= quad_x[0][1] and quad_y[1][0] <= r.y <= quad_y[1][1]:
            counts[2] += 1
        elif quad_x[1][0] <= r.x <= quad_x[1][1] and quad_y[1][0] <= r.y <= quad_y[1][1]:
            counts[3] += 1
    
    print(counts)
    return counts

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x 
        self.y = y 
        self.vx = vx 
        self.vy = vy

    def step(self,max_x, max_y):
        self.x = (self.x + self.vx) % max_x 
        if self.x < 0:
            self.x += max_x 

        self.y = (self.y + self.vy) % max_y 
        if self.y < 0:
            self.y += max_y 


if __name__ == "__main__":

    robots = []

    filename = "14-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()
    pattern = "p\=(\d+),(\d+)\sv=(\-*\d+),(\-*\d+)"
    for l in lines:
        x = re.match(pattern, l)
        if x:
            robots.append(Robot(int(x.group(1)),int(x.group(2)),int(x.group(3)),int(x.group(4))))

    for i in range(cycles):
        for r in robots:
            r.step(x_max, y_max)
    
    counts = count_quadrants(robots)
    print(counts[0] * counts[1] * counts[2] * counts[3])

