
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

def solve_system(monkeys):
    keys = (monkeys['root'][0], monkeys['root'][2])
    while isinstance(monkeys['root'], list):
        for name, val in monkeys.items():
            if isinstance(val,list):
                if isinstance(monkeys[val[0]],int) and isinstance(monkeys[val[2]],int):
                    monkeys[name] = do_op(monkeys[val[0]], val[1], monkeys[val[2]])
    return monkeys['root'], monkeys[keys[0]] == monkeys[keys[1]]

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

if __name__ == "__main__":

    #p1
    monkeys = populate_monkeys()
    val, keys_match = solve_system(monkeys)

    print(val, keys_match)

    #p2
    i = -1
    keys_match = False 
    while not keys_match:
        i += 1
        monkeys = populate_monkeys()
        monkeys['humn'] = i 
        val,keys_match = solve_system(monkeys)
    print(i)
        