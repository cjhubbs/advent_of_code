if __name__ == "__main__":

    #p1
    filename = "01-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    up = lines[0].count('(')
    down = lines[0].count(')')

    print("p1:", up - down)
    floor = 0
    for index, c in enumerate(lines[0]):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            print("p2: ", index+1)
            break 
