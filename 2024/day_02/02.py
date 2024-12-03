def validate(x):
    
    levels = x.copy()
    prev = levels.pop(0)
    next = levels[0]
    if next > prev: #increasing
        while(levels):
            next = levels.pop(0)
            if not (next - prev) in range(1,4):
                return False
            else:
                prev = next
        return True
    elif prev > next:
        while(levels):
            next = levels.pop(0)
            if not (prev - next) in range(1,4):
                return False
            else:
                prev = next
        return True
    else:
        return False


if __name__ == "__main__":

    filename = "02-input.txt"
    threshold = 1

    with open(filename) as f:
        lines = f.read().splitlines()
    safe_count = 0

    for l in lines:
        removal_counter = 0
        levels = [int(n) for n in l.split()]

        #check for natural good
        if validate(levels):
            safe_count += 1
        else:
            for i in range(len(levels)):
                temp = levels.copy()
                temp.pop(i)
                if validate(temp):
                    safe_count += 1
                    break 

    print(safe_count)