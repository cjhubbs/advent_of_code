def getPoss(rules, r):
    poss = []
    if rules[r][0][0] == '"b"':
        return ["b"]
    elif rules[r][0][0] == '"a"':
        return ["a"]

    for o in rules[r]:
        if len(o) == 1:
            poss += getPoss(rules, o[0])
        else:
            p1 = getPoss(rules, o[0])
            p2 = getPoss(rules, o[1])
            poss += [x+y for x in p1 for y in p2]

    return poss

def part1(data):
    rules = {}
    for line in data[0]:
        line = line.split(": ")
        sub = line[1]
        if "|" in sub:
            sub = sub.split(" | ")
        else:
            sub = [sub]
        for i in range(len(sub)):
            sub[i] = sub[i].split(" ")

        rules[line[0]] = sub

    print(rules)
    
    c = 0
    poss = getPoss(rules, '0')
    # print(poss)
    for line in data[1]:
        if line in poss:
            c += 1

    return c

data = [[],[]]
f = open("input19.txt","r")
dd = f.read().splitlines()
f.close()
for d in dd:
	if ":" in d:
		data[0].append(d)
	else:
		data[1].append(d)
print(part1(data))

