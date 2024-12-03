import re

if __name__ == "__main__":

    #p1
    filename = "03-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    pattern = 'mul\((\d{1,3}),(\d{1,3})\)'

    total = 0
    for l in lines:
        m = re.findall(pattern,l)
        for pair in m:
            total += int(pair[0]) * int(pair[1])
    print(total)

    #p2
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()
    pattern = 'mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don)\'t\(\)'

    total = 0
    enabled = True
    for l in lines:
        matches = re.findall(pattern,l)
        for m in matches:
            if m[3] == 'don':
                enabled = False 
            elif m[2] == 'do':
                enabled = True 
            else:
                if enabled:
                    total += int(m[0]) * int(m[1])
    print(total)
