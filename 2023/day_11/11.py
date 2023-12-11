
def find_empty_rows_cols(g):
    empty_rows = []
    empty_cols = []
    empty_row = "." * len(g[0])
    for index, row in enumerate(g):
        if row == empty_row:
            empty_rows.append(index)
    for col in range(len(g[0])):
        empty_col = True
        for row in range(len(g)):
            if g[row][col] != '.':
                empty_col = False    
        if empty_col:
            empty_cols.append(col)
    return empty_rows, empty_cols

def find_points(g):
    points = []
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] == "#":
                p = [row,col]
                points.append(p)
    return points

def sum_distances(points):
    sum = 0
    for index, p in enumerate(points):
        for i in range(index+1,len(points)):
            sum += abs(p[1] - points[i][1]) + abs(p[0] - points[i][0])
    return sum

if __name__ == "__main__":
    with open('11-input.txt') as f:
      lines = f.read().splitlines()
    points = find_points(lines)
    empty_rows, empty_cols = find_empty_rows_cols(lines)
    expansion_factor = 999999
    for row in reversed(empty_rows):
        for p in points:
            if p[0] > row:
                p[0] += expansion_factor
    for col in reversed(empty_cols):
        for p in points:
            if p[1] > col:
                p[1] += expansion_factor
    dist = sum_distances(points)
    print('dist: ', dist)