if __name__ == "__main__":

    filename = "05-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    rules = {}
    total = 0

    #p1
    for l in lines:
        if "|" in l:
            before, after = l.split("|")
            if after in rules.keys():
                rules[after].append(before)
            else:
                rules[after] = [before]
        
        if "," in l:
            valid = True
            pages = l.split(",")
            i = 0
            while i < len(pages):
                if pages[i] in rules.keys():
                    for j in range(i+1,len(pages)):
                        if pages[j] in rules[pages[i]]:
                            valid = False 
                            break
                i += 1
            if valid:
                middle_idx = int((len(pages) - 1) / 2)
                total += int(pages[middle_idx])

    print(total)
