with open('10-input.txt') as f:
    lines = f.read().splitlines()
f.close()

values = [1]

for l in lines:
    chars = l.split()
    values.append(values[-1])
    if chars[0] == "addx":
        values.append(values[-1] + int(chars[1]))

total = 0
for i in range(20,260,40):
    total += (values[i-1]*i)
print("P1:", total)

pixels = []
for i in range(240):
    if abs(values[i] - (i % 40)) < 2:
        pixels.append("#")
    else:
        pixels.append(".")

print("Part 2:")
for i in range(0,260,40):
    print("".join(pixels[i:i+40]))
