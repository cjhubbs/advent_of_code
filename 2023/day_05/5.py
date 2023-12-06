import re 

class Mapping():
    def __init__(self,dest,source, length):
        self.dest = int(dest)
        self.source = int(source)
        self.length = int(length)
    
    def do_mapping(self,n):
        if self.source <= n <= self.source + self.length:
            return self.dest + (n - self.source)
        else:
            return n 

class Map():
    def __init__(self,source,dest):
        self.source = source 
        self.dest = dest 
        self.mappings = []

    def add_mapping(self,m):
        self.mappings.append(m)

    def do_mapping(self,n):
        temp = 0
        for m in self.mappings:
            temp = m.do_mapping(n)
            if temp != n:
                return temp
        return temp 

p1_seeds = []
p2_seeds = []
maps = []
maps.append(Map('seed','soil'))
maps.append(Map('soil','fertilizer'))
maps.append(Map('fertilizer','water'))
maps.append(Map('water','light'))
maps.append(Map('light','temperature'))
maps.append(Map('temperature','humidity'))
maps.append(Map('humidity','location'))

def parse_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
    phase = -1
    for l in lines:
        if re.search('seeds:',l):
            parts = l.split(':')    
            seed_list = parts[1].split()
            [p1_seeds.append(int(s)) for s in seed_list]
            for i in range(0,len(seed_list),2):
                for n in range(int(seed_list[i+1])):
                    p2_seeds.append(int(seed_list[i]) + n)

        else:
            new_phase = re.search('(.+)\smap:',l)
            if new_phase:
                phase += 1
            if re.search('\d+ \d+ \d+',l):
                nums = l.split()
                maps[phase].add_mapping(Mapping(nums[0],nums[1],nums[2]))

def process_seeds(seeds):
    results = []
    for s in seeds:
        input = s
        for m in maps:
            input = m.do_mapping(input)
        results.append(input)
    print("min result: ",min(results))
    return min(results)

if __name__ == "__main__":
    parse_input('5-input.txt')
    process_seeds(p1_seeds)
    process_seeds(p2_seeds)
