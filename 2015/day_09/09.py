import itertools 

if __name__ == "__main__":

    filename = "09-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    stops = set()
    distances = {}

    for l in lines:
        tokens = l.split()
        source = tokens[0]
        target = tokens[2]
        dist = tokens[4]

        stops.add(source)
        stops.add(target)
        if source not in distances.keys():
            distances[source] = {}
        if target not in distances.keys():
            distances[target] = {}
        distances[source][target] = int(dist)
        distances[target][source] = int(dist)
    
    brute_force_routes = list(itertools.permutations(stops,len(stops)))
    min_dist = 10000000
    max_dist = 0
    for route in brute_force_routes:
        dist = 0
        for i in range(len(route)-1):
            dist += distances[route[i]][route[i+1]]
        min_dist = min(dist,min_dist)
        max_dist = max(dist,max_dist)
    print("p1:",min_dist)
    print("p2:",max_dist)
