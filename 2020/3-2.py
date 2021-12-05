
def count_trees(content, x_increment, y_increment):
    tree_count=0
    x=0
    y=0
    width=len(content[0])

    while y < len(content)-1:
        x=(x+x_increment) % width
        y=y+y_increment
        print (str(x) + ", " + str(y))
        if content[y][x] == "#":
            tree_count += 1
    return tree_count

with open("input3.txt") as f:
    slope = f.readlines()
slope = [x.strip() for x in slope]

result1 = count_trees(slope, 1,1)
result2 = count_trees(slope,3,1)
result3 = count_trees(slope,5,1)
result4 = count_trees(slope,7,1)
result5 = count_trees(slope,1,2)

total = result1 * result2 * result3 * result4 * result5
print (str(total))
