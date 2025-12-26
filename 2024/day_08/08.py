from itertools import combinations 
from operator import add, sub

def node_in_range(n):
    return 0 <= n[0] < max_rows and 0 <= n[1] < max_cols

def calc_possible_nodes(p, limit):
    dist = (list( map(sub, p[1], p[0]) ))
    nodes = [p[1],p[0]]
    temp = p[0]
    count = 0
    while node_in_range(list(map(sub,temp,dist))):
        if limit and (count == 1): 
            break
        nodes.append(temp)
        temp = list(map(sub,temp,dist))
        count += 1
    temp = p[1]
    count = 0
    while node_in_range(list(map(add,temp,dist))):
        if limit and (count == 1): 
            break
        nodes.append(list(map(add,temp,dist)))
        temp = list(map(add,temp,dist))
        count += 1
    return nodes


if __name__ == "__main__":

    filename = "08-test2.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    max_rows = len(lines)
    max_cols = len(lines[0])

    ant = {}
    antinodes = {}

    for r_idx,r in enumerate(lines):
        for c_idx,c in enumerate(r):
            if c != '.':
                if c in ant.keys():
                    ant[c].append([r_idx,c_idx])
                else:
                    ant[c] = [[r_idx, c_idx]]
    
    for a in ant.values():
        for pair in combinations(a,2):
            n = calc_possible_nodes(pair,False)
            print(n)
            for node in n:
                antinodes[','.join(str(node))] = 1
    print(len(antinodes))