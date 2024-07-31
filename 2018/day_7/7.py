import copy
import re

class Worker:
    def __init__(self):
        self.timer = 0
        self.state = "idle"
        self.letter = ""
    
    def task(self,letter):
        self.letter = letter 
        self.state = "working"
        self.timer = ord(letter) - 4
    
    def update(self):
        if self.state == "working":
            self.timer -= 1
            if self.timer == 0:
                self.state = "idle"
                return self.letter 
            else:
                return None
        else:
            return None

def get_idle_worker(workers):
    for w in workers:
        if w.state == "idle":
            return w 
    return None

def any_worker_active(workers):
    for w in workers:
        if w.state == "working":
            return True
    return False


if __name__ == "__main__":

    parents = {}
    all_nodes = set()
    available_nodes = set()
    used_nodes = set()
    ops = ""

    f = open("input-7.txt", "r")
    lines = f.read().splitlines()
    for l in lines:
        #Step F must be finished before step E can begin.
        x = re.match("Step (\w{1}) must be finished before step (\w{1}) can begin",l)
        node = x.groups()[1]
        parent = x.groups()[0]
        parents.setdefault(node,[]).append(parent)
        all_nodes.add(node)
        all_nodes.add(parent)

    p2_parents = copy.deepcopy(parents) 
    p2_all_nodes = set(all_nodes) 

    #p1
    while parents:
        available_nodes = all_nodes - used_nodes 
        available_nodes = available_nodes - set(parents.keys())
        next_node = sorted(available_nodes)[0]
        ops += next_node
        used_nodes.add(next_node)
        for k,v in parents.items():
            if next_node in v:
                parents[k].remove(next_node)
        parent_keys = list(parents.keys())
        for k in parent_keys:
            if len(parents[k]) == 0:
                del(parents[k])

    ops += parent_keys[0]               
    print(ops)

    #p2
    step_count = -1
    workers = []
    used_nodes = set()
    for i in range(5):
        workers.append(Worker())

    while p2_parents or any_worker_active(workers):
        step_count += 1
        for w in workers:
            done = w.update()
            if done:
                for k,v in p2_parents.items():
                    if done in v:
                        p2_parents[k].remove(done)
                parent_keys = list(p2_parents.keys())
                for k in parent_keys:
                    if len(p2_parents[k]) == 0:
                        del(p2_parents[k])


        available_nodes = all_nodes - used_nodes 
        available_nodes = available_nodes - set(p2_parents.keys())
        currently_available = sorted(available_nodes)

        while currently_available:
            w = get_idle_worker(workers)
            if w:
                next_node = currently_available[0]
                w.task(next_node)
                used_nodes.add(next_node)
                currently_available.pop(0)

            else:
                break 

    print(step_count)
        
