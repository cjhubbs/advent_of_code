
if __name__ == "__main__":

    filename = "01-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()

    dial = 50
    delta = 0
    zero_count = 0

    for l in lines:
        if l[0] == "L":
            delta = -1
        else:
            delta = 1
        count = int(l[1:])
        for i in range(count):
            dial += delta 
            if dial == -1:
                dial = 99 
            elif dial == 100:
                dial = 0
            if dial == 0:
                zero_count += 1
    
    print("zero count:", zero_count)