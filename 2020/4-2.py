import fileinput
import re

def check_validity(f):
    valid_list_1 = ["byr", "cid", "ecl","eyr","hcl","hgt","iyr","pid"]
    valid_list_2 = ["byr", "ecl","eyr","hcl","hgt","iyr","pid"]
    valid_eye_colors = ["amb","blu","brn","gry","grn","hzl","oth"]

    k = list(f.keys())
    k.sort()
    if k == valid_list_1 or k == valid_list_2:
        all_valid = 1
        for key, value in f.items():
            if key == "byr":
                year = re.search("^\d{4}$",value)
                if int(year.group()) >= 1920 and int(year.group()) <= 2002:
                else:
                    all_valid = 0
            if key == "cid":
                pass
            if key == "ecl":
                if value in valid_eye_colors:
                    pass 
                else:
                    all_valid = 0
            if key == "eyr":
                year = re.search("^\d{4}$",value)
                if int(year.group()) >= 2020 and int(year.group()) <= 2030:
                    pass 
                else:
                    all_valid = 0
            if key == "hcl":
                if re.search("^\#[0-9a-f]{6}$",value):
                    pass 
                else:
                    all_valid = 0
            if key == "hgt":
                cm = re.search("^\d{3}cm$",value)
                inches = re.search("^\d{2}in$",value)
                if cm:
                    num = re.search("\d{3}",cm.group())
                    if int(num.group()) >= 150 and int(num.group()) <= 193:
                        pass 
                    else:
                        all_valid = 0
                elif inches:
                    num = re.search("\d{2}",inches.group())
                    if int(num.group()) >= 59 and int(num.group()) <= 76:
                        pass 
                    else:
                        all_valid = 0
                else:
                    all_valid = 0
            if key == "iyr":
                year = re.search("^\d{4}$",value)
                if int(year.group()) >= 2010 and int(year.group()) <= 2020:
                    pass 
                else:
                    all_valid = 0
            if key == "pid":
                if re.search("^\d{9}$",value):
                    pass 
                else:
                    all_valid = 0
        if all_valid == 1:
            return 1
        else:
            return 0
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