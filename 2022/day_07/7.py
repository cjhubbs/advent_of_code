import re

dir_sizes = []

class Node:
    def __init__(self, name, kind, parent, size=0):
        self.size = int(size)
        self.name = name
        self.parent = parent 
        self.children = []
        self.kind = kind
        if parent is not None:
            parent.children.append(self) 

    def get_child_dir(self, child_name):
        for c in self.children:
            if c.kind == "dir" and c.name == child_name:
                return c 
        return None
    
    def calc_tree_sizes(self):
        for c in self.children:
            if c.kind == "dir":
                c.calc_tree_sizes()
            self.size += c.size
        dir_sizes.append(self.size)
    
if __name__ == "__main__":
    root = Node("/", "dir", None)  
    current_node = root  

    with open('7-input.txt') as f:
        lines = f.read().splitlines()

    cd_pattern = re.compile(r'\$ cd (.+)$')
    ls_pattern = re.compile(r'^\$ ls')
    dir_pattern = re.compile(r'^dir (.+)')
    file_pattern = re.compile(r'^(\d+)\s(.+)')
    
    for l in lines:
        match = cd_pattern.search(l)
        if match:
            if match.group(1) == "/":
                current_node = root 
            elif match.group(1) == "..":
                current_node = current_node.parent 
            else:
                current_node = current_node.get_child_dir(match.group(1))

        match = ls_pattern.search(l)
        if match:
            pass 
    
        match = dir_pattern.search(l)
        if match:
            n = Node(match.group(1),"dir",current_node)

        match = file_pattern.search(l)
        if match:
            n = Node(match.group(2), "file", current_node, match.group(1))
    
    root.calc_tree_sizes()
    total = 0
    for s in dir_sizes:
        if s <= 100000:
            total += s
    print("P1 sizes: ",total)

    current_free_space = 70000000 - root.size
    need_to_del = 30000000 - current_free_space
    dir_sizes.sort()
    for s in dir_sizes:
        if s > need_to_del:
            print("P2 delete", s)
            break
