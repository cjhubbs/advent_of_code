def getval(token,gates):
    if token.isdigit():
        return True, int(token)
    else:
        if token in gates.keys():
            return True, gates[token]
        else:
            return False, -1     

def getv(token,gates):
    if token.isdigit():
        return int(token)
    else:
        return gates[token]

def all_keys_available(tokens,gates):
    if tokens[1] in ["RSHIFT","LSHIFT","AND","OR"]:
        v1,val1 = getval(tokens[0],gates)
        v2,val2 = getval(tokens[2],gates)
        return v1 and v2 
    elif tokens[0] == "NOT":
        v1,val = getval(tokens[1],gates)
        return v1
    else:
        v1,val = getval(tokens[0],gates)
        return v1

def iterate_for_a(lines,gates):

    idx = 0
    while not ("a" in gates.keys()):
        l = lines[idx]
        tokens = l.split()
        if tokens[-1] not in gates.keys():
            if all_keys_available(tokens,gates):
                val = 0
                if "RSHIFT" in l:
                    val = getv(tokens[0],gates) >> int(tokens[2])
                elif "LSHIFT" in l: 
                    val = getv(tokens[0],gates) << int(tokens[2])
                elif "AND" in l:
                    val = getv(tokens[0],gates) & getv(tokens[2],gates)
                elif "OR" in l:
                    val = getv(tokens[0],gates) | getv(tokens[2],gates)
                elif "NOT" in l:
                    val = ~ getv(tokens[1],gates)
                else:
                    val = getv(tokens[0],gates)
        
                gates[tokens[-1]] = val
        idx += 1
        if idx > len(lines)-1:
            idx = 0
    return gates["a"]

if __name__ == "__main__":

    filename = "07-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    gates = {}

    #P1
    p1_answer = iterate_for_a(lines,gates)
    print(p1_answer)

    #P2
    gates = {}
    gates['b'] = p1_answer 
    p2_answer = iterate_for_a(lines,gates)
    print(p2_answer)
