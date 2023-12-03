import copy

def do_op(v1, op, v2):
    if op == "+":
        return v1 + v2 
    if op == "-":
        return v1 - v2 
    if op == "*":
        return v1 * v2 
    if op == "/":
        return int(v1 / v2)
    else:
        return -1

def build_stack(root, monkeys):
    stack = []

def solve_system(monkeys, root):
    prev_monkeys = copy.deepcopy(monkeys)

    while isinstance(monkeys[root], list):
        for name, val in monkeys.items():
            if isinstance(val,list):
                if isinstance(monkeys[val[0]],int) and isinstance(monkeys[val[2]],int):
                    monkeys[name] = do_op(monkeys[val[0]], val[1], monkeys[val[2]])
        if monkeys == prev_monkeys:
            break
        prev_monkeys = copy.deepcopy(monkeys)
    return monkeys

def populate_monkeys():
    monkeys = {}

    with open('21-input.txt') as f:
        lines = f.read().splitlines()
    f.close()
    for l in lines:
        tokens = l.split()
        if len(tokens) == 2:
            monkeys[tokens[0].strip(":")] = int(tokens[1])
        else:
            monkeys[tokens[0].strip(":")] = tokens[1:]
    return monkeys

def fill_in_terms(monkeys):
    for name, val in monkeys.items():
        if isinstance(val,list):
            if isinstance(monkeys[val[0]],int):
                monkeys[name][0] = monkeys[val[0]]
            if isinstance(monkeys[val[2]],int):
                monkeys[name][2] = monkeys[val[2]]
    return monkeys

if __name__ == "__main__":

    #p1
    monkeys = populate_monkeys()
    solution = solve_system(monkeys,'root')
    print(solution['root'])

    #p2
    l_monkeys = populate_monkeys()
    r_monkeys = populate_monkeys()
    root_tokens = (l_monkeys['root'][0], l_monkeys['root'][2])
    l_monkeys['humn'] = 'x'
    r_monkeys['humn'] = 'x'
    left_sol = solve_system(l_monkeys, root_tokens[0])
    right_sol = solve_system(r_monkeys, root_tokens[1])

    left_sol = fill_in_terms(left_sol)
    right_sol = fill_in_terms(right_sol)

    for name,val in left_sol.items():
        if not isinstance(val,int):
            print(name, val)
    print("==============================================")
    for name,val in right_sol.items():
        if not isinstance(val,int):
            print(name, val)

        