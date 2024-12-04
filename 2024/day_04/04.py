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

if __name__ == "__main__":

    #p1
    filename = "04-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()
    rows = len(lines)
    cols = len(lines[0])

    count = 0
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "X":
                count += check_xmas(r,c,lines)
    print(count)