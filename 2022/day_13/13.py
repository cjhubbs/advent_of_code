import json
import functools
  
def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    elif isinstance(a, int):
        return compare([a],b)
    elif isinstance(b, int):
        return compare(a,[b])
    elif a and b:
        q = compare(a[0], b[0])
        return q if q else compare(a[1:], b[1:])
    return 1 if a else (-1 if b else 0)

if __name__ == "__main__":

    with open('13-input.txt') as f:
        lines = f.read().splitlines()
    f.close()

    index_sum = 0
    index = 0
    p2_lines = []

    #part 1
    while lines:
        index += 1
        l1 = json.loads(lines.pop(0).strip())
        l2 = json.loads(lines.pop(0).strip())
        p2_lines.append(l1)
        p2_lines.append(l2)
        blank = lines.pop(0)
        result = compare(l1, l2)
        if result == -1:
            index_sum += index
    print("P1 answer:", index_sum)
  
    p2_lines.append([[2]])
    p2_lines.append([[6]])
    p2_lines = sorted(p2_lines,key=functools.cmp_to_key(compare))

    print("P2 key: ", (p2_lines.index([[2]])+1) * (p2_lines.index([[6]])+1))
