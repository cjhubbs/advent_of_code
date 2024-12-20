import itertools

def do_calc(operands, operators):
    temp = operands[0]
    for i in range(len(operators)):
        if operators[i] == "*":
            temp = temp * operands[i+1]
        elif operators[i] == "+":
            temp = temp + operands[i+1]
        elif operators[i] == "|":
            temp = int(str(temp) + str(operands[i+1]))
    return temp

if __name__ == "__main__":
    filename = "07-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    p1_calibration_result = 0
    p2_calibration_result = 0
    p1_possible_operators = ["+", "*"]
    p2_possible_operators = ["+", "*", "|"]


    for l in lines:
        temp = l.split()
        target = int(temp[0][:-1])
        operands = [int (x) for x in temp[1:]]

        for ops in itertools.product(p1_possible_operators,repeat=(len(operands)-1)):
            #print(ops)
            result = do_calc(operands, ops)
            if result == target:
                p1_calibration_result += target
                break

        for ops in itertools.product(p2_possible_operators,repeat=(len(operands)-1)):
            #print(ops)
            result = do_calc(operands, ops)
            if result == target:
                p2_calibration_result += target
                break

    print(p1_calibration_result)
    print(p2_calibration_result)