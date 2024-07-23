f = open("input-1.txt", "r")
steps = f.read().splitlines()

freq = 0
freqs = {}

#p1
for x in steps:
    if x[0] == "+":
        freq += int(x[1:])
    else:
        freq -= int(x[1:])
print("freq is: ", freq)

#p2
step = 0
freq = 0
while 1:
    if steps[step][0] == "+":
        freq += int(steps[step][1:])
    else:
        freq -= int(steps[step][1:])
    keys = freqs.keys()
    if freq in keys:
        print("double: ", freq)
        break 
    else:
        freqs[freq] = 1
    step = (step + 1) % len(steps)
