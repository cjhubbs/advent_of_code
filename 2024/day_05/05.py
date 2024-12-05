rules = {}

def check(pages):
    global rules 
    valid = True
    i = 0
    while i < len(pages):
        if pages[i] in rules.keys():
            for j in range(i+1,len(pages)):
                if pages[j] in rules[pages[i]]:
                    valid = False 
                    break
        i += 1
    return valid

def score(pages):
    return int(pages[int((len(pages) - 1) / 2)])

def repair(pages):
    temp = pages 
    i = 0
    while i < len(temp):
        if temp[i] in rules.keys():
            for j in range(i+1,len(temp)):
                if temp[j] in rules[temp[i]]:
                    temp_char = temp.pop(i)
                    temp.insert(j,temp_char)
                    i = -1
                    break
        i += 1

    return temp

if __name__ == "__main__":

    filename = "05-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    p1_total = 0
    p2_total = 0

    #p1
    count = 1
    for l in lines:
        if "|" in l:
            before, after = l.split("|")
            if after in rules.keys():
                rules[after].append(before)
            else:
                rules[after] = [before]
        
        if "," in l:
            pages = l.split(",")
            if check(pages):
                p1_total += score(pages)
                print(f"{count}: valid")
            else:
                #p2
                temp = repair(pages)
                p2_total += score(temp)
                print(f"{count}: fixed")
            count += 1
    print(p1_total)
    print(p2_total)
