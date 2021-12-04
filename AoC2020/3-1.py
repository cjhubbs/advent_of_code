with open("input3.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
width=len(content[0])

tree_count=0
x=0
y=0

while y < len(content)-1:
    x=(x+3) % width
    y=y+1
    print (str(x) + ", " + str(y))
    if content[y][x] == "#":
        tree_count += 1
print(tree_count)
