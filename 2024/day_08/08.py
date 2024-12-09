from itertools import combinations 
from operator import add, sub

def calc_possible_nodes(p):
    dist = (list( map(sub, p[1], p[0]) ))
    nodes = []
    nodes.append(list(map(sub,p[0],dist)))
    nodes.append(list(map(add,p[1],dist)))
    return nodes

def node_in_range(n):
    return 0 <= n[0] < max_rows and 0 <= n[1] < max_cols

if __name__ == "__main__":

    filename = "08-input.txt"

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
            n = calc_possible_nodes(pair)
            print(n)
            for node in n:
                if node_in_range(node):
                    antinodes[','.join(str(node))] = 1
    print(len(antinodes))