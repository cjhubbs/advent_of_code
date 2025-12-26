
x_vec = []
y_vec = []

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

if __name__ == "__main__":

    f = open("input-6-test.txt", "r")
    lines = f.read().splitlines()
    for l in lines:
        x,y=l.split(',')
        x_vec.append(int(x))
        y_vec.append(int(y))
    x_min = min(x_vec)
    x_max = max(x_vec)
    y_min = min(y_vec)
    y_max = max(y_vec)

    num_of_points = len(x_vec)
    point_counts = [0]*num_of_points

    for x_pt in range (x_min, x_max):
        for y_pt in range(y_min, y_max):
            distance_to_point = {}
            for i in range(num_of_points):
                dist = manhattan(x_pt, y_pt, x_vec[i],y_vec[i])
                if dist in distance_to_point.keys():
                    break 
                else:
                    distance_to_point[dist] = i 
            min_pt = min(distance_to_point, key=distance_to_point.get)
            point_counts[min_pt] += 1
    print(point_counts)
