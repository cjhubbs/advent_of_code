import re 
import itertools

class Planet():
    def __init__(self, x, y,z):
        self.pos = [x,y,z]
        self.vel = [0,0,0]
    
    def apply_gravity(self,other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
                other.vel[i] -= 1
            elif self.pos[i] > other.pos[i]:
                self.vel[i] -= 1
                other.vel[i] += 1

    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
    def energy(self):
        pot = 0
        kin = 0
        for i in range(3):
            pot += abs(self.pos[i])
            kin += abs(self.vel[i])
        return pot * kin

    def matches(self,other):
        return self.pos == other.pos and self.vel == other.vel

    def print(self):
        print('pos=[',self.pos[0],',',self.pos[1],',',self.pos[2],'], vel=[',self.vel[0],',',self.vel[1],',',self.vel[2],']')

if __name__ == "__main__":

    planets = []
    initial_planets = []

    with open('12-input.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        o = re.match('.*\=(.*)\,.*\=(.*)\,.*\=(.*)\>',l)
        planets.append(Planet(int(o.group(1)),int(o.group(2)),int(o.group(3))))
        initial_planets.append(Planet(int(o.group(1)),int(o.group(2)),int(o.group(3))))
    num_of_planets = len(planets)

    pairs = list(itertools.combinations(range(num_of_planets),2))

    found_all_matches = False
    found_match = [-1] * num_of_planets
    hits = []
    for i in range(num_of_planets):
        hits.append({})
    counter = 0
    while not found_all_matches:
        counter += 1
        for p in pairs:
            planets[p[0]].apply_gravity(planets[p[1]])
        for p in planets:
            p.apply_velocity()

        #p1
        if counter == 1000:
            total_energy = sum([p.energy() for p in planets])
            print("p1 total_energy: ", total_energy)
            break



 