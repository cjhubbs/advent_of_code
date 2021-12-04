from collections import namedtuple
import re 

Node = namedtuple("Node","isTerminal letter number firstChildren secondChildren")

f = open("input19.txt","r")
data = f.read().splitlines()
f.close()

rules = {}
valid_strings = {}

def generate_strings(n,s):
	global rules
	global valid_strings
	tmp = ""
	if n.isTerminal:
		s += n.letter
		return s
	else:
		tmp = generate_strings(rules[n.firstChildren[0]],s)
		if len(n.firstChildren) > 1:
			tmp  = generate_strings(rules[n.firstChildren[1]],tmp)
		if rules[n.firstChildren[-1]].isTerminal:
			valid_strings[tmp] = 1
		if len(n.secondChildren) > 0:
			tmp = generate_strings(rules[n.secondChildren[0]],s)
			if len(n.secondChildren) > 1:
				tmp = generate_strings(rules[n.secondChildren[1]],tmp)
			if rules[n.secondChildren[-1]].isTerminal:
				valid_strings[tmp] = 1
		return tmp

test_strings = []

for d in data:
	rule = re.match('^(\d+): (.+)$',d)
	if rule:
		#print(rule.group(1))
		paths = rule.group(2).split('|')
		#print(paths)
		if len(paths) == 1:
			if paths[0] == '"a"':
				rules[rule.group(1)] = Node(1,'a',rule.group(1),[],[])
			elif paths[0] == '"b"':
				rules[rule.group(1)] = Node(1,'b',rule.group(1),[],[])
			else:
				nums = paths[0].strip().split(" ")
				#print(nums)
				rules[rule.group(1)] = Node(0,'',rule.group(1),nums,[])
		else:
			first_nums = paths[0].strip().split(" ")
			second_nums = paths[1].strip().split(" ")
			rules[rule.group(1)] = Node(0,'',rule.group(1),first_nums,second_nums)
	else:
		ip = re.match('^([ab]+)$',d)
		if ip:
			test_strings.append(ip.group(1).strip())
	
#print(rules)
#print(test_strings)
generate_strings(rules['0'],"")
print(valid_strings)
count =0
for vs in test_strings:
	if vs in valid_strings.keys():
		count += 1
print(count)
