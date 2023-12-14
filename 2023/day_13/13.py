def number_of_diffs(s1,s2):
    difference_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            difference_count += 1
    return difference_count

def check_reflection(part, m,index):
    rows = min(index+1,len(m)-(index+1))
    smudge_counter = 0
    for i in range(rows):
        r1 = m[index-i]
        r2 = m[index + i + 1]
        if part == 1:
            if r1 != r2:
                return False 
        else:
            if number_of_diffs(r1,r2) == 1:
                smudge_counter += 1
            elif number_of_diffs(r1,r2) > 1:
                return False
    if part == 2 and smudge_counter != 1:
        return False
    return True

def find_row_reflection(part, m):
    for index, line in enumerate(m):
        if index < len(m)-1:
            if part == 1:
                if line == m[index+1]:
                    if check_reflection(part, m,index):
                        return index + 1
            else:
                if line == m[index+1] or (number_of_diffs(line,m[index+1]) == 1):
                    if check_reflection(part, m,index):
                        return index + 1
    return 0 

def transpose(m):
    return [''.join(s) for s in zip(*m)]
   

if __name__ == "__main__":
    mirrors = []
    with open('13-input.txt') as f:
      lines = f.read().splitlines()
    m = []
    for l in lines:
        if l == '':
           mirrors.append(m)
           m = []
        else:
           m.append(l)
    mirrors.append(m)
    
    sum = 0
    for m in mirrors:
        val = find_row_reflection(1,m)
        if val == 0:
           m1 = transpose(m)
           val = find_row_reflection(1,m1)
           sum += val
        else:
            sum += val*100
    print(sum)

    sum = 0
    for m in mirrors:
        val = find_row_reflection(2,m)
        if val == 0:
           m1 = transpose(m)
           val = find_row_reflection(2,m1)
           sum += val
        else:
            sum += val*100
    print(sum)