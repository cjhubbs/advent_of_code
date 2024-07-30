import re

if __name__ == "__main__":

    parents = {}
    all_nodes = set()
    available_nodes = set()
    used_nodes = set()
    ops = ""

    f = open("input-7.txt", "r")
    lines = f.read().splitlines()
    for l in lines:
        #Step F must be finished before step E can begin.
        x = re.match("Step (\w{1}) must be finished before step (\w{1}) can begin",l)
        node = x.groups()[1]
        parent = x.groups()[0]
        parents.setdefault(node,[]).append(parent)
        all_nodes.add(node)
        all_nodes.add(parent)

    while parents:
        available_nodes = all_nodes - used_nodes 
        available_nodes = available_nodes - set(parents.keys())
        next_node = sorted(available_nodes)[0]
        ops += next_node
        used_nodes.add(next_node)
        for k,v in parents.items():
            if next_node in v:
                parents[k].remove(next_node)
        parent_keys = list(parents.keys())
        for k in parent_keys:
            if len(parents[k]) == 0:
                del(parents[k])

    ops += parent_keys[0]               
    
    #p1
    print(ops)

    