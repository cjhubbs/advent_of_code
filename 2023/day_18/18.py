dir_offset = {'U': [-1,0],
              'D': [1,0],
              'L': [0,-1],
              'R': [0,1]}

dir_translator = {'0': 'R',
                  '1': 'D',
                  '2': 'L',
                  '3': 'U'}

def shoelace(points):
    result = 0
    for i in range(len(points)-1):
        x1,y1 = points[i]
        x2,y2 = points[i+1]
        result += x1*y2 - x2*y1
    return abs(result) // 2

if __name__ == "__main__":
    cur = [0,0]
    with open('18-input.txt') as f:
        lines = f.read().splitlines()

    points = []
    perimeter = 0
    for l in lines:
        contents = l.split()
        
        #p1
        #pos = contents[0]
        #mag = int(contents[1])

        #p2
        pos = dir_translator[contents[2][-2]]
        mag = int(contents[2][2:7],16)
        cur = [cur[0] + mag*dir_offset[pos][0],cur[1] + mag*dir_offset[pos][1]]
        perimeter += mag

        points.append(cur)
    area = shoelace(points)
    print(area + perimeter // 2 + 1)    