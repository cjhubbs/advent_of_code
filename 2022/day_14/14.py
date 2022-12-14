def parse_input(lines):
    p = {}
    max_y = 0
    
    for l in lines:
        points = l.split(" -> ")
        for i in range(len(points)-1):
            x1, y1 = points[i].split(",")    
            x2, y2 = points[i+1].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            if x1==x2:
                if y1 < y2:
                    start_y = y1
                    end_y = y2 
                else:
                    start_y = y2 
                    end_y = y1
                for y in range(start_y, end_y+1):
                    p[(x1,y)] = "#"
            else:
                if x1 < x2:
                    start_x = x1
                    end_x = x2 
                else:
                    start_x = x2 
                    end_x = x1
                for x in range(start_x, end_x+1):
                    p[x,y1] = "#"
            if max(y1,y2) > max_y:
                max_y = max(y1,y2)
    return p, max_y

def loop_sand(p,pos, prev_pos, max_y):
    while pos[1] < max_y and pos != prev_pos:
        prev_pos = pos

        down = (pos[0],pos[1]+1)
        down_left = (pos[0]-1,pos[1]+1)
        down_right = (pos[0]+1, pos[1]+1)

        if down not in p.keys():
            pos = down
        elif down_left not in p.keys():
            pos = down_left 
        elif down_right not in p.keys():
            pos = down_right 
    return pos

def drop_sand_into_abyss(p, max_y):
    pos = (500,0)
    prev_pos = (-1, -1)
    pos = loop_sand(p,pos,prev_pos, max_y)
    if pos[1] < max_y:
        p[pos] = "O"
        return p
    else:
        return -1

def fill_with_sand(p,floor):
    count = 0
    entry = (500,0)
    prev_pos = (-1, -1)
    while entry not in p.keys():
        count += 1
        pos = entry
        prev_pos = (-1, -1)
        pos = loop_sand(p,pos, prev_pos,floor)
        p[pos] = "O"
    return count

if __name__ == "__main__":

    with open('14-input.txt') as f:
        lines = f.read().splitlines()
    f.close()
    p1, max_y = parse_input(lines)
    p2, max_y = parse_input(lines)
    print("max y: ",max_y)
    count = 0
    while True:
        p = drop_sand_into_abyss(p1,max_y)
        if p == -1:
            print(count)
            break
        else:
            count += 1
    
    print(fill_with_sand(p2,max_y + 1))
