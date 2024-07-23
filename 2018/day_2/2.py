def count_letters(s):
    counts = {}
    for c in s:
        if c in counts.keys():
            counts[c]+=1
        else:
            counts[c] = 1
    return counts.values()

f = open("input-2.txt", "r")
boxes = f.read().splitlines()

#p1
has_a_double = 0
has_a_triple = 0
for b in boxes:
    c = count_letters(b)
    if 2 in c:
        has_a_double += 1
    if 3 in c:
        has_a_triple += 1

print("checksum is: ", has_a_triple*has_a_double)

#p2
for box in range(len(boxes)):
    for other in range(box+1,len(boxes)):
        distance = sum(x != y for x,y in zip(boxes[box],boxes[other]))
        if distance == 1:
            print("dist 1: ", boxes[box],boxes[other])