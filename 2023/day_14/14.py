import copy 

def find_furthest_north(m,row,col):
    new_row = row
    if new_row == 0:
        return 0
    while ((new_row > 0) and (m[new_row-1][col] == '.')):
        new_row = new_row - 1
    return new_row 

def find_furthest_south(m,row,col):
    new_row = row
    if new_row == len(m):
        return row
    while ((new_row < len(m)-1) and (m[new_row+1][col] == '.')):
        new_row = new_row + 1
    return new_row 

def find_furthest_east(m,row,col):
    new_col = col
    if new_col == len(m[0]):
        return col
    while ((new_col < len(m)-1) and (m[row][new_col+1] == '.')):
        new_col = new_col + 1
    return new_col 

def find_furthest_west(m,row,col):
    new_col = col
    if new_col ==  0:
        return 0
    while ((new_col > 0) and (m[row][new_col-1] == '.')):
        new_col = new_col - 1
    return new_col 

def tilt(m,direction):
    if direction == 'n':
        for col in range(len(m[0])):
            for row in range(len(m)):
                if m[row][col] == 'O':
                    new_row = find_furthest_north(m,row,col)
                    m[row][col] = '.'
                    m[new_row][col] = 'O'
    if direction == 's':
        for col in range(len(m[0])):
            for row in reversed(range(len(m))):
                if m[row][col] == 'O':
                    new_row = find_furthest_south(m,row,col)
                    m[row][col] = '.'
                    m[new_row][col] = 'O'
    if direction == 'w':
        for row in range(len(m)):
            for col in range(len(m[0])):
                if m[row][col] == 'O':
                    new_col = find_furthest_west(m,row,col)
                    m[row][col] = '.'
                    m[row][new_col] = 'O'
    if direction == 'e':
        for row in range(len(m)):
            for col in reversed(range(len(m[0]))):
                if m[row][col] == 'O':
                    new_col = find_furthest_east(m,row,col)
                    m[row][col] = '.'
                    m[row][new_col] = 'O'
    return m     

def do_one_rotation(m):
    m = tilt(m,'n')
    m = tilt(m,'w')
    m = tilt(m,'s')
    m = tilt(m,'e')
    return m

def calc_weight(m):
    max_weight = len(m)
    sum = 0
    for index,row in enumerate(m):
        sum += row.count('O') * (max_weight - index)
    return sum

def arrays_are_equal(a,b):
    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] != b[row][col]:
                return False
    return True

def duplicate_detected(cache,m):
    for index, c in enumerate(cache):
        if arrays_are_equal(c,m):
            return index 
    return -1

if __name__ == "__main__":
    with open('14-input.txt') as f:
      lines = f.read().splitlines()
      lines = [list(l) for l in lines]
    m = tilt(lines,'n')
    weight = calc_weight(m)
    print('p1:' , weight)

    #p2
    max_cycles = 1000000000
    m = copy.deepcopy(lines) 
    cache = []

    #do 1 rotation
    m = do_one_rotation(m)
    cache.append(copy.deepcopy(m))

    counter = 0
    while True:
        counter += 1
        m = do_one_rotation(m)
        dup_index = duplicate_detected(cache,m)
        if dup_index != -1:
            print('found match: cache = ',dup_index," counter = ",counter)
            break
        cache.append(copy.deepcopy(m))
    rem_factor = counter - dup_index
    rem = (max_cycles - dup_index) % rem_factor 
    m = copy.deepcopy(lines)
    for i in range(rem + dup_index):
        m = do_one_rotation(m)

    weight = calc_weight(m)
    print('p2:', weight)