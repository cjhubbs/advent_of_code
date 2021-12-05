f = open("input2.txt", "r")
ok_count = 0
for x in f:
    line = x.split()
    positions = line[0].split("-")
    first_index = int(positions[0]) - 1
    second_index = int(positions[1]) - 1
    char_to_check = line[1][0]
    string_to_check = line[2]
    match1 = string_to_check[first_index] == char_to_check
    match2 = string_to_check[second_index] == char_to_check
    if match1 != match2:
        ok_count+=1
print(ok_count)
