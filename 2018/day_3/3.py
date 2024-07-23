import re 

f = open("input-3.txt", "r")
claims = f.read().splitlines()
ids = []
points = {}
for c in claims:
    x = re.match("\#(\d+) @ (\d+),(\d+)\: (\d+)x(\d+)",c)
    id = x.groups()[0]
    ids.append(id)
    col = int(x.groups()[1])
    row = int(x.groups()[2])
    cols = int(x.groups()[3])
    rows = int(x.groups()[4])
    for r in range(row,row+rows):
        for c in range(col,col+cols):
            k = str(r) + "," + str(c)
            if k in points.keys():
                points[k].append(id)
            else:
                points[k] = [id]

#p1
overlap = sum(len(x) > 1 for x in points.values())
print(overlap)

#p2
for p in points.values():
    #more than one claim on this spot, so remove all claiming IDs
    if len(p) > 1:
        for i in p:
            if i in ids: ids.remove(i)

#the only one left will be the one that doesn't overlap at all
print(ids)