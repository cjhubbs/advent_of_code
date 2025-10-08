if __name__ == "__main__":
    filename = "02-input.txt"

    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    paper = 0
    ribbon = 0
    for l in lines:
        dims = list(map(int,(l.split('x'))))
        dims.sort()

        paper += 3*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[0]*dims[2]
        ribbon += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]
    
    print(paper)
    print(ribbon)
