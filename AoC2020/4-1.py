import fileinput

def check_validity(f):
    print(f)
    valid_list_1 = ["byr", "cid", "ecl","eyr","hcl","hgt","iyr","pid"]
    valid_list_2 = ["byr", "ecl","eyr","hcl","hgt","iyr","pid"]
    k = list(f.keys())
    k.sort()
    print (k)
    if k == valid_list_1 or k == valid_list_2:
        return 1
    else:
        return 0

fields = {}

total_valid = 0

for line in fileinput.input():
    if line == "\n":
        total_valid += check_validity(fields)
        fields = {}
    else:
        params = line.split()
        for p in params:
            kv = p.split(":")
            fields[kv[0]] = kv[1]

print("total valid: " + str(total_valid))
