times = []
distances = []
single_time = 0
single_dist = 0

def parse_input(file):
    global single_time 
    global single_dist 
    with open(file) as f:
        lines = f.read().splitlines()
    times.extend([int(t) for t in lines[0].split(':')[1].split()])
    distances.extend([int(d) for d in lines[1].split(':')[1].split()])
    single_time = int(lines[0].split(':')[1].replace(" ",""))
    single_dist = int(lines[1].split(':')[1].replace(" ",""))

def find_race_options(time,dist):
    winners = 0
    for t in range(time):
        d = t * (time-t)
        if d > dist:
            winners +=1 
    return winners

if __name__ == "__main__":
    parse_input('06-input.txt')
    p1_total = 1
    for i in range(len(times)):
        p1_total *= find_race_options(times[i],distances[i])
    print(p1_total)
    p2_total = find_race_options(single_time,single_dist)
    print(p2_total)

