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
    
    return temp

if __name__ == "__main__":

    filename = "05-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    p1_total = 0
    p2_total = 0

    #p1
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
            else:
                #p2
                temp = repair(pages)
                p2_total += score(temp)

    print(p1_total)
    print(p2_total)
