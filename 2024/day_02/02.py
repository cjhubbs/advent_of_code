

if __name__ == "__main__":

    filename = "02-input.txt"
    threshold = 0

    with open(filename) as f:
        lines = f.read().splitlines()
    safe_count = 0

    for l in lines:
        removal_counter = 0
        levels = [int(n) for n in l.split()]
        last_level = levels[0]
        safe = True
        if levels[1] > levels[0]: #increasing
            for n in range(1,len(levels)):
                if not (levels[n] - last_level) in range(1,4):
                    removal_counter += 1
                    if not (levels[n+1] - last_level in range(1,4)):
                        safe = False
                last_level = levels[n]
            if removal_counter > threshold:
                safe = False
        elif levels[0] > levels[1]: #decreasing
            for n in range(1,len(levels)):
                if not (last_level - levels[n]) in range(1,4):
                    removal_counter += 1
                last_level = levels[n]
            if removal_counter > threshold:
                safe = False
        else:
            safe = False
        if safe:
            safe_count += 1
    print(safe_count)