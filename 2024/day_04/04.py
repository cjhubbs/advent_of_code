rows = 0
cols = 0

def check_xmas(r,c,lines):
    dirs = { 
            'UP': { 'delta_r': -1,
                    'delta_c': 0 },
            'DN': { 'delta_r': 1,
                    'delta_c': 0 },
            'LL': { 'delta_r': 0,
                    'delta_c': -1 },
            'RR': { 'delta_r': 0,
                    'delta_c': 1 },
            'UR': { 'delta_r': -1,
                    'delta_c': 1 },
            'UL': { 'delta_r': -1,
                    'delta_c': -1 },
            'DR': { 'delta_r': 1,
                    'delta_c': 1 },
            'DL': { 'delta_r': 1,
                    'delta_c': -1 }
           }
    
    count = 0
    for key,d in dirs.items():
        if 0 <= r + (d['delta_r']*3) < rows and 0 <= c + (d['delta_c']*3) < cols:
            if (lines[r+d['delta_r'] * 1][c+d['delta_c'] * 1] == "M" and 
                lines[r+d['delta_r'] * 2][c+d['delta_c'] * 2] == "A" and
                lines[r+d['delta_r'] * 3][c+d['delta_c'] * 3] == "S"):
               count += 1
    return count

def check_x(r,c,lines):
    if 0 < r < (rows-1) and 0 < c < (cols-1):
        if ((lines[r+1][c+1] == "M" and lines[r+1][c-1] == "M" and lines[r-1][c+1] == "S" and lines[r-1][c-1] == "S") or
            (lines[r+1][c+1] == "S" and lines[r+1][c-1] == "S" and lines[r-1][c+1] == "M" and lines[r-1][c-1] == "M") or
            (lines[r+1][c+1] == "M" and lines[r+1][c-1] == "S" and lines[r-1][c+1] == "M" and lines[r-1][c-1] == "S") or
            (lines[r+1][c+1] == "S" and lines[r+1][c-1] == "M" and lines[r-1][c+1] == "S" and lines[r-1][c-1] == "M")):
           return 1
        
    return 0
    
if __name__ == "__main__":

    #p1
    filename = "04-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()
    rows = len(lines)
    cols = len(lines[0])

    p1_count = 0
    p2_count = 0
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "X":
                p1_count += check_xmas(r,c,lines)
            if lines[r][c] == "A":
                p2_count += check_x(r,c,lines)
    print(p1_count)
    print(p2_count)

