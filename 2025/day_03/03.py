
def process_string(s,new_string, remaining_digits):
    line_length = len(s)
    window = line_length - remaining_digits + 1
    substring = s[:window]
    dig = max(list(substring))
    idx = s.index(dig)
    new_string += dig 
    if remaining_digits > 1:
        new_string = process_string(s[idx+1:],new_string,remaining_digits-1)
    return new_string 

if __name__ == "__main__":

    filename = "03-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()

    #p1 
    total = 0
    for l in lines:
        dig1 = max(list(l[0:-1]))
        idx1 = l.index(dig1)
        dig2 = max(list(l[idx1+1:]))
        val = int(dig1 + dig2)
        total += val 
    print("p1 total: ",total)

    #p2
    total = 0
    for l in lines:
        dig_string = process_string(l,"",12)
        total += int(dig_string)  
    print(total)