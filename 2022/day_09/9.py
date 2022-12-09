
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = {}
    
    def is_touching(self,p):
        touching = False 
        x_dist = abs(self.x - p.x)
        y_dist = abs(self.y - p.y)
        if x_dist < 2 and y_dist < 2:
            touching = True 
        return touching 
    
    def is_two_steps_direct(self,tail):
        x_dist = self.x - tail.x
        y_dist = self.y - tail.y
        if x_dist == 2 and y_dist == 0:
            return 1, 0, True
        elif x_dist == -2 and y_dist == 0:
            return -1, 0, True
        elif x_dist == 0 and y_dist == 2:
            return 0, 1, True
        elif x_dist == 0 and y_dist == -2:
            return 0, -1, True
        else:
            return 0,0, False
    
    def move_diagonally_toward(self,head):
        delta_x = head.x - self.x
        delta_y = head.y - self.y 
        if delta_x > 0:
            self.x += 1
        else:
            self.x -= 1
        if delta_y > 0:
            self.y += 1
        else:
            self.y -= 1

    def log_point(self):
        point_str = str(self.x) + "," + str(self.y)
        self.visited[point_str] = 1

class Rope():
    def __init__(self, num_of_points):
        self.num_of_points = num_of_points
        self.points = []
        for i in range(self.num_of_points):
            self.points.append(Point(0,0))
        self.points[-1].log_point()

    def process_step(self,x_step, y_step):
        self.points[0].x += x_step 
        self.points[0].y += y_step 

        for i in range(1,self.num_of_points):

            if not self.points[i-1].is_touching(self.points[i]):
                
                #this will return a step in the right direction if it is two steps away in an ordinal direction
                step_x, step_y, stepped = self.points[i-1].is_two_steps_direct(self.points[i])
                self.points[i].x += step_x 
                self.points[i].y += step_y

                if not stepped:
                    self.points[i].move_diagonally_toward(self.points[i-1])
            
        self.points[-1].log_point()

    def process_command(self, direction, magnitude):
        x_step = 0
        y_step = 0
        match direction:
            case "U":
                y_step = 1
            case "D":
                y_step = -1
            case "L":
                x_step = -1
            case "R":
                x_step = 1
        for i in range(magnitude):
            self.process_step(x_step, y_step)
    def tail(self):
        return self.points[-1]

if __name__ == "__main__":
    p1 = Rope(2) 
    p2 = Rope(10)

    with open('9-input.txt') as f:
        lines = f.read().splitlines()
    f.close()

    for l in lines:
        chars = l.split()
        p1.process_command(chars[0], int(chars[1]))
        p2.process_command(chars[0], int(chars[1]))
    
    print("P1:", len(p1.tail().visited))
    print("P2:", len(p2.tail().visited))

