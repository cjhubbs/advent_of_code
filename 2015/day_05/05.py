import re 

def contains_repeated_pair(s):
    for i in range(len(s)-1):
        check_string = s[i:i+2]
        num = s.count(check_string)
        if num > 1:
            return True 
    return False

def contains_span(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True 
    return False

if __name__ == "__main__":

    filename = "05-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    naughty = 0
    nice = 0

    for l in lines:
        vowels = 0
        prev_char = ''
        found_double = False
        if "ab" in l or "cd" in l or "pq" in l or "xy" in l:
            naughty += 1
        else:
            for c in l:
                if c in ["a","e","i","o","u"]:
                    vowels += 1
                if c == prev_char:
                    found_double = True 
                prev_char = c 
            if vowels > 2 and found_double:
                nice += 1
            else:
                naughty += 1
    print("p1:")
    print("nice: ",nice)
    print("naughty: ",naughty)

#p2
    naughty = 0
    nice = 0

    for l in lines:
        if contains_repeated_pair(l) and contains_span(l):
            nice += 1
        else:
            naughty += 1
    print("p2:")
    print("nice: ",nice)
    print("naughty: ",naughty)
