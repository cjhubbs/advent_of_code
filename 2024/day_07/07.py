import itertools
import operator 


def do_calc(operands, operators):
    temp = operands[0]
    for i in range(len(operators)):
        temp = operators[i](temp,operands[i+1])
    return temp

if __name__ == "__main__":
    filename = "07-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    calibration_result = 0
    possible_operators = [operator.add, operator.mul]


    for l in lines:
        temp = l.split()
        target = int(temp[0][:-1])
        operands = [int (x) for x in temp[1:]]

        for ops in itertools.product(possible_operators,repeat=(len(operands)-1)):
            #print(ops)
            result = do_calc(operands, ops)
            if result == target:
                calibration_result += target
                break
    
    #p1
    print(calibration_result)