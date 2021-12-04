import re 

class Bag:

	def __init__(self, color):
		self.color = color
		self.parents = []
		self.children = {}
	
	def addParent(self, parent):
		self.parents.append(parent)
	
	def addChild(self, child,number):
		self.children[child] = number
	
	def gatherParents(self, d):
		
		if self.parents:
			for p in self.parents:
				d[p.color] = 1
				d = p.gatherParents(d)
		return d

bags = {}
all_parents = {}
pattern = '([\w\s]+) bags contain (.+$)'
p = re.compile(pattern)
child_pattern = '(\d+) ([\w\s]+) bag'
cp = re.compile(child_pattern)

f = open("input7.txt", "r")
for l in f:
	stuff = p.search(l)
	bag_color = stuff.group(1)
	if not bag_color in bags:
		bags[bag_color] = Bag(bag_color)
	
	rest = stuff.group(2)
	children = rest.split(',')
	for c in children:
		line = cp.search(c)
		if line:
			child_bag_color = line.group(2)
			child_bag_count = line.group(1)
			if not child_bag_color in bags:
				bags[child_bag_color] = Bag(child_bag_color)
			bags[bag_color].addChild(bags[child_bag_color],child_bag_count)
			bags[child_bag_color].addParent(bags[bag_color])

my_bag = bags['shiny gold']
temp_dict = {}
all_parents = my_bag.gatherParents(temp_dict)
print(all_parents)
print(len(all_parents))
	
