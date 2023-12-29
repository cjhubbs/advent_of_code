pulse_counter = {-1:0,1:0}
modules = {}

class FlipFlop():
    def __init__(self,label, connections):
        self.state = False
        self.connections = connections
        self.label = label
    def process_pulse(self,p,q,sender):
        if p < 0:
            self.state = not self.state
            out_val = -1
            if self.state:
                out_val = 1
            for c in self.connections:
                global pulse_counter 
                global modules
                pulse_counter[out_val] += 1
                q.append(tuple([self.label,c,out_val]))

            
class Conjunction():
    def __init__(self,label, connections):
        self.inputs = {}
        self.connections = connections 
        self.label = label
    def add_input(self,i):
        self.inputs[i] = -1
    def process_pulse(self,p,q,sender):
        self.inputs[sender] = p
        if all (x == 1 for x in self.inputs.values()):
            out_val = -1
        else:
            out_val = 1
        for c in self.connections:
            global pulse_counter 
            global modules
            pulse_counter[out_val] += 1
            q.append(tuple([self.label,c,out_val]))

if __name__ == "__main__":
    with open('20-input.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        parts = l.split('->')

        if parts[0][0] == '%':
            label = parts[0][1:].strip()
            connections = parts[1].strip().split(', ')
            modules[label] = FlipFlop(label,connections)
        elif parts[0][0] == '&':
            label = parts[0][1:].strip()
            connections = parts[1].strip().split(', ')
            modules[label] = Conjunction(label,connections)
        elif 'broadcaster' in parts[0]:
            pulse_targets = [p.strip() for p in parts[1].split(', ')]
    #print(modules)
    for m in modules.values():
        if m.__class__ == Conjunction:
            for n in modules.values():
                if m.label in n.connections:
                    m.add_input(n.label)
    #print(modules)

    pulse_queue = []
    button_presses = 1000
    for i in range(button_presses):
        for t in pulse_targets:
            pulse_queue.append(tuple(['broadcaster',t,-1]))
            pulse_counter[-1] += 2
        while pulse_queue:
            p = pulse_queue.pop(0)
            #print(p)
            if p[1] in modules:
                modules[p[1]].process_pulse(p[2],pulse_queue,p[0])

    print(pulse_counter)
    print(pulse_counter[-1] * pulse_counter[1])