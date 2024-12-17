
def create_map(s):
    map = []
    id = 0
    block = True
    for d in s:
        if block:
            for k in range(int(d)):
                map.append(id)
            id += 1
            block = False
        else:
            for k in range(int(d)):
                map.append(".")
            block = True
    return map

def condense(old):
    new_map = []
    while(old):
        next = old.pop(0)
        if next == ".":
            temp = old.pop(-1)
            while temp == ".":
                temp = old.pop(-1)
            new_map.append(temp)
        else:
            new_map.append(next)
    return new_map

def calc_checksum(m):
    checksum = 0
    for i, val in enumerate(m):
        checksum += (i*val)
    return checksum

if __name__ == "__main__":
    filename = "09-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    old_map = create_map(lines[0])
    #print(old_map)
    new_map = condense(old_map)
    #print(new_map)
    print(calc_checksum(new_map))
