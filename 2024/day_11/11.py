input = "4329 385 0 1444386 600463 19 1 56615"

def left_trim(s):
    non_zero = False 
    temp = ""
    for c in s:
        if c != "0":
            non_zero = True
        if non_zero:
            temp = temp + c 
    if temp == "":
        temp = "0"
    return temp

def blink(rocks):
    new_rocks = {}
    for key,count in rocks.items():
        if key == "0":
            if not "1" in new_rocks.keys():
                new_rocks["1"] = 0
            new_rocks["1"] += count
        elif len(key) % 2 == 0:
            half_len = int(len(key)/2)
            first_half = key[:half_len]
            second_half = left_trim(key[(half_len):])
            if not first_half in new_rocks.keys():
                new_rocks[first_half] = 0
            new_rocks[first_half] += count 
            if not second_half in new_rocks.keys():
                new_rocks[second_half] = 0
            new_rocks[second_half] += count
        else:
            temp = str(int(key)*2024)
            new_rocks[temp] = count 
    return new_rocks

if __name__ == "__main__":
    rck = {}
    for r in input.split(" "): 
        rck[r] = 1
        
    iterations = 75   
    for i in range(iterations):
        rck = blink(rck)
    
    total = 0
    for v in rck.values():
        total += v 
    print(total)