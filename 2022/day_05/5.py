import re 
import string

class Cargo:
    def __init__(self):
        self.num_of_stacks = 0
        self.stack_lines = []
        self.stacks = []
        self.move_lines = []
    
    def top_string(self):
        s = ""
        for i in self.stacks:
            if len(i) > 0:
                s = s + i[-1]
        return s

    def add_to_stack(self, stack, crate):
        self.stacks[stack].append(crate)
    
    def move(self, fr, to):
        self.stacks[to].append(self.stacks[fr].pop())
    
    def move_multi(self, fr, to, num):
        index = len(self.stacks[fr]) - num
        for i in range(num):
            self.stacks[to].append(self.stacks[fr].pop(index))

    def parse(self, lines):
        stack_pattern = re.compile(r'\s*\[\w\]')
        index_pattern = re.compile(r'^\s+\d')
        move_pattern = re.compile('move')
        for l in lines:
            if stack_pattern.match(l):
                self.stack_lines.append(l)
            elif index_pattern.match(l):
                self.num_of_stacks = len(l.split()) 
                for i in range(self.num_of_stacks + 1):
                    self.stacks.append([])
            elif move_pattern.match(l):
                self.move_lines.append(l)
        
        for l in reversed(self.stack_lines):
            for i in range(0,self.num_of_stacks):
                index = 1 + i*4
                if l[index] in string.ascii_uppercase:
                    self.add_to_stack(i+1,l[index])

    def do_moves(self, part):
        p = re.compile(r'\d+')
        for l in self.move_lines:
            indices = p.findall(l)
            if part == 1:
                for i in range(int(indices[0])):
                    self.move(int(indices[1]), int(indices[2]))
            else:
                self.move_multi(int(indices[1]), int(indices[2]), int(indices[0]))

if __name__ == "__main__":
    lines = []
    with open('5-input.txt') as f:
        lines = f.read().splitlines()
    p1 = Cargo()
    p1.parse(lines)
    p1.do_moves(1)
    print(p1.top_string())

    p2 = Cargo()
    p2.parse(lines)
    p2.do_moves(2)
    print(p2.top_string())