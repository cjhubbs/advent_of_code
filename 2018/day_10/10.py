import re 
import matplotlib.pyplot as plt 
from collections import namedtuple 

if __name__ == "__main__":

    x = []
    y = []
    dx = []
    dy = []
    cycle_count = 0

    f = open("input-10.txt", "r")
    lines = f.read().splitlines()
    num_points = len(lines)
    for l in lines:
        m = re.match("position=<\s*(\-*\d+),\s*(\-*\d+)>\s*velocity=<\s*(\-*\d+),\s*(\-*\d+)>",l)
        x.append(int(m.groups()[0]))
        y.append(int(m.groups()[1]))
        dx.append(int(m.groups()[2]))
        dy.append(int(m.groups()[3]))

    while abs(max(x, key=abs)) > 240 and abs(max(y, key=abs)) > 240:
        for i in range(len(x)):
            x[i] += dx[i]
            y[i] += dy[i]
        cycle_count += 1

    plt.scatter(x,y)
    plt.show()    
    while 1:
        for i in range(len(x)):
            x[i] += dx[i]
            y[i] += dy[i]
        cycle_count += 1
        print(cycle_count)
        plt.scatter(x,y)
        plt.show()    
