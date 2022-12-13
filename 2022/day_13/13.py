import re

def parse_line(l):
    list_stack = [] 
    num_str = ""
    for c in l:
        if c == "[":
            list_stack.append([])
        elif c.isdigit():
            num_str += c 
        elif c == ",":
            if num_str != "":
                list_stack[-1].append(int(num_str))
                num_str = ""
        elif c == "]":
            if num_str != "":
                list_stack[-1].append(int(num_str))
                num_str = ""
            tmp = list_stack.pop(-1)
            if list_stack == []:
                return tmp
            else:
                list_stack[-1].append(tmp)
    
def numbers_in_order(left,right):
    if left > right:
        return -1
    elif left == right:
        return 0
    else:
        return 1 

def lists_in_order(l1, l2):
    while l1 and l2:
        left = l1.pop(0)
        right = l2.pop(0)
        if isinstance(left,int) and isinstance(right,int):
            inorder = numbers_in_order(left, right)
        elif isinstance(left,list) and isinstance(right,list):
            inorder = lists_in_order(left,right)
        elif isinstance(left,list):
            right = [right]
            inorder = lists_in_order(left,right)
        else: #right is list, left is int
            left = [left]
            inorder = lists_in_order(left,right)
        if inorder != 0:
            return inorder 
    if l2: #l1 had less items, lists are in order
        return 1
    elif l1:
        return -1
    else:
        return 0

def string_to_list(s,l):
    temp_str = ""
    for c in s:
        if c == "[":
            pass 
        elif c.isnumeric():
            temp_str += c 
        elif c == "," or c == "]":
            if temp_str:
                l.append(int(temp_str))
                temp_str = ""
    return l 

if __name__ == "__main__":

    with open('13-input.txt') as f:
        lines = f.read().splitlines()
    f.close()

    index_sum = 0
    index = 0
    p2_lines = []

    #part 1
    while lines:
        index += 1
        p2_lines.append(lines.pop(0).strip())
        p2_lines.append(lines.pop(0).strip())
        l1 = parse_line(p2_lines[-2])
        l2 = parse_line(p2_lines[-1])
        blank = lines.pop(0)
        result = lists_in_order(l1, l2)
        if result == 1:
            index_sum += index
    print(index_sum)

    num_lines = []
    no_num_lines = []
    
    for l in p2_lines:
        if re.findall("\d",l):
            num_lines.append(string_to_list(l,[]))
        else:
            no_num_lines.append(l)
    print("Num lines:")
    num_lines = sorted(num_lines)
    print(num_lines)
    print("No Num lines:")
    print(sorted(no_num_lines))

    f = open("numlines.txt", "a")
    for l in no_num_lines:
        f.write(l)
        f.write("\n")
    for l in num_lines:
        f.write(",".join(map(str,l)))
        f.write("\n")
    f.close()

    last_1 = -1
    last_5 = -1
    index = len(no_num_lines) + 1
    for l in num_lines:
        if last_1 == -1 and l[0] > 1:
            last_1 = index
            index += 1 
        if last_5 == -1 and l[0] > 5:
            last_5 = index
        index += 1
    print(last_1)
    print(last_5)
    
    print("P2 key: ", last_1*last_5)
