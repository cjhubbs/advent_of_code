import re

class Rule():
    def __init__(self,s):
        self.has_condition = False 
        if ':' in s:
            self.has_condition = True 
            self.param = s[0]
            self.operator = s[1]
            parts = s.split(':')
            self.target = parts[1]
            self.threshold = int(parts[0][2:])
        else:
            self.target = s
    
    def constraint(self):
        if self.has_condition:
            return self.param + self.operator + str(self.threshold) + ":" + self.target
        else:
            return self.target
    
    def is_terminal(self):
        return self.target in ['R','A']

    def process(self, part):
        if not self.has_condition:
            return True, self.target 
        else:
            if self.operator == "<":
                if part[self.param] < self.threshold:
                    return True, self.target 
                else:
                    return False,'' 
            else:
                if part[self.param] > self.threshold:
                    return True, self.target 
                else:
                    return False,''
                
def parse_input_row(s):
    parts = s.split(',')
    rules = []
    [rules.append(Rule(p)) for p in parts]
    return rules

def parse_part_row(s):
    x = {}
    temp = s[1:-1]
    params = temp.split(',')
    for p in params:
        t = p.split('=')
        x[t[0]] = int(t[1])
    return x 

def process_workflow(workflows, part):
    step = 'in'
    while True:
        for rule in workflows[step]:
            found, target = rule.process(part)
            if found:
                step = target 
                break
        if step == 'A' or step == 'R':
            break
    if step == 'A':
        return sum(part.values())
    else:
        return 0

def assemble_paths(workflows,path,tag):
    node = workflows[tag]
    for rule in node:
        path.append(rule.constraint())
        if rule.is_terminal():
            if rule.target == "A":
                print("found A", path)
            path.pop()
        else:
            assemble_paths(workflows, path, rule.target)
            path.pop()
    return

if __name__ == "__main__":
    with open('19-test.txt') as f:
        lines = f.read().splitlines()
    workflows = {}
    parts = []
    p1_sum = 0
    for l in lines:
        if len(l)>0:
            if l[0].isalnum():
                parts = l.split('{')
                rules = parts[1][:-1]
                workflows[parts[0]] = parse_input_row(rules)
            else:
                p = parse_part_row(l)
                p1_sum += process_workflow(workflows, p)

    print(p1_sum)
    assemble_paths(workflows,[],'in')