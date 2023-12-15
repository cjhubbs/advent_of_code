boxes = [dict() for x in range(256)]

def hash_line(l):
    h = 0
    for char in l:
        h += ord(char)
        h *= 17
        h = h % 256
    return h

if __name__ == "__main__":
    with open('15-input.txt') as f:
      lines = f.read().splitlines()[0].split(',')

    p1_total = sum([hash_line(l) for l in lines])
    print('p1: ',p1_total)

    for l in lines:
        split_char = '-'
        if '=' in l:
            split_char = '='

        parts = l.split(split_char)
        label = parts[0]
        box = hash_line(label)
        if split_char == '=':
            power = int(parts[1])
            boxes[box][label] = power
        elif label in boxes[box]:
            del boxes[box][label] 
    p2_total = 0
    for index, box in enumerate(boxes):
        if box:
            counter = 1
            for v in box.values():
                p2_total += ((index+1) * counter * v)
                counter += 1
    print('p2: ',p2_total)

