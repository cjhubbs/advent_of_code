
def find_furthest_north(m,row,col):
    new_row = row
    if new_row == 0:
        return 0
    while ((new_row > 0) and (m[new_row-1][col] == '.')):
        new_row = new_row - 1
    return new_row 
    
def tilt_north(m):
    for col in range(len(m[0])):
        for row in range(len(m)):
            if m[row][col] == 'O':
                new_row = find_furthest_north(m,row,col)
                m[row][col] = '.'
                m[new_row][col] = 'O'
    return m     

def calc_weight(m):
    max_weight = len(m)
    sum = 0
    for index,row in enumerate(m):
        sum += row.count('O') * (max_weight - index)
    return sum

if __name__ == "__main__":
    with open('14-input.txt') as f:
      lines = f.read().splitlines()
      lines = [list(l) for l in lines]
    m = tilt_north(lines)
    weight = calc_weight(m)
    print(weight)