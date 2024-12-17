
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

def calc_block_checksum(blocks):
    checksum = 0
    for idx,data in blocks.items():
        for i in range(data[1]):
            checksum += ((idx+i)*data[0])
    return checksum

def calc_blocks(s):
    s = s + "0"
    idx = 0
    blocks = {}
    blanks = {}
    id = 0
    while len(s) > 0:
        data = int(s[0])
        empty = int(s[1])
        s = s[2:]
        blocks[idx] = [id,data]
        idx += data 
        blanks[idx] = empty 
        idx += empty
        id += 1
    return blocks, blanks


if __name__ == "__main__":
    filename = "09-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    old_map = create_map(lines[0])
    old = old_map.copy()
    new_map = condense(old_map)

    #p1
    print(calc_checksum(new_map))

    blocks, blanks = calc_blocks(lines[0])
    print(blocks)
    print(blanks)
    new_blocks = blocks.copy()

    for block_idx,block_len in reversed(blocks.items()):
        for gap_idx,gap_len in blanks.items():
            if gap_len >= block_len[1]:
                new_blocks[gap_idx] = block_len 
                del blanks[gap_idx]
                del new_blocks[block_idx]
                if gap_len > block_len[1]:
                    blanks[gap_idx + block_len[1]] = (gap_len - block_len[1])
                break 
        blanks = dict(sorted(blanks.items()))

    new_blocks = dict(sorted(new_blocks.items()))
    #print(new_blocks)
    print(calc_block_checksum(new_blocks))
