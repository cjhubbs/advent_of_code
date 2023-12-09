def process_line(l):
    n = l.split()
    n = [[int(x) for x in n]]
    tier = 0
    while not all(i == 0 for i in n[tier]):
       tier += 1
       n.append([])
       for k in range(len(n[tier-1])-1):
          n[tier].append(n[tier-1][k+1] - n[tier-1][k])
    
    #p1
    for k in reversed(range(len(n)-1)):
       n[k].append(n[k][-1] + n[k+1][-1])
    p1_result = n[0][-1]
    
    #p2
    for k in reversed(range(len(n)-1)):
       n[k].insert(0,n[k][0] - n[k+1][0])
    p2_result = n[0][0]
    
    return p1_result, p2_result

if __name__ == "__main__":
    with open('09-input.txt') as f:
      lines = f.read().splitlines()
    p1_total = 0
    p2_total = 0
    for l in lines:
       p1, p2 = process_line(l)
       p1_total += p1 
       p2_total += p2 
    print("p1: ", p1_total)
    print("p2: ", p2_total)