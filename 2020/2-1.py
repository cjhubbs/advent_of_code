f = open("input2.txt", "r")
ok_count = 0
for x in f:
    line = x.split()
    print(line)
    counts = line[0].split("-")
    count_min = counts[0]
    count_max = counts[1]
    char_to_count = line[1][0]
    string_to_check = line[2].strip()
    #print(count_min + count_max + char_to_count + string_to_check)
    count = string_to_check.count(char_to_count)
    print(count)    
    if count >= int(count_min) and count <= int(count_max):
        print("found one")
        ok_count+=1

print(ok_count)
