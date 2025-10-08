def visit(visited,x,y):
    idx = str(x) + "," + str(y)
    if idx in visited.keys():
        visited[idx] += 1
    else:
        visited[idx] = 0

def update_pos(dir,x,y):
    new_x = x 
    new_y = y
    if dir == "^":
        new_y += 1
    elif dir == "v":
        new_y -= 1
    elif dir == ">":
        new_x += 1
    elif dir == "<":
        new_x -= 1 
    return new_x, new_y

if __name__ == "__main__":

    filename = "03-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    visited = {}
    x = 0
    y = 0
    visit(visited,x,y)
    for c in lines[0]:
        x,y = update_pos(c,x,y)
        visit(visited,x,y)
    print("p1: ", len(visited))

    visited = {}
    s_x = 0
    s_y = 0
    r_x = 0
    r_y = 0
    visit(visited,0,0)
    idx = 0
    while idx < len(lines[0]):
        s_x, s_y = update_pos(lines[0][idx],s_x,s_y)
        visit(visited,s_x,s_y)
        r_x, r_y = update_pos(lines[0][idx+1],r_x,r_y)
        visit(visited,r_x,r_y)
        idx += 2
    print("p2: ", len(visited))
