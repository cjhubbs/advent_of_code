class Cup:
	def __init__(self,value):
		self.val = value
		self.next = None
		self.prev = None

class LList:
	def __init__(self):
		self.head_value = None
		self.tail_value = None
		self.circle = {}

	def append(self,c):
		self.circle[c.val] = c 
		
		# insert into empty list
		if self.head_value == None:
			self.head_value = c.val
	
		# for everything other than empty list, set next for prev
		if self.tail_value != None:
			self.circle[self.tail_value].next = c.val
		
		#set prev for this element
		c.prev = self.tail_value
		c.next = None
		self.tail_value = c.val
		
	def link_ends(self):
		self.circle[self.head_value].prev = self.tail_value
		self.circle[self.tail_value].next = self.head_value
	
	def extract(self,k):
		cup = self.circle[k]
		self.circle[cup.prev].next = cup.next
		self.circle[cup.next].prev = cup.prev
		del self.circle[k]
		return cup
	
	def retrieve(self,k):
		if k in self.circle.keys():
			return self.circle[k]
		else:
			return None
		
	def insert_after(self,old,new):
		new.next = old.next
		old.next = new.val
		new.prev = old.val
		self.circle[new.next].prev = new.val
		self.circle[new.val] = new
		
	def print_list(self):
		s = ""
		index = self.head_value
		s += str(self.circle[index].val) + " "
		while self.circle[index].next != self.head_value:
			index = self.circle[index].next
			s += str(self.circle[index].val) + " "
		print(s)
		return 
		
	def check_consistency(self):
		count = 0
		pointer = self.head_value
		count += 1
		while self.circle[pointer].next != self.head_value:
			pointer = self.circle[pointer].next
			count += 1
		print("count forward = " + str(count))
		count = 0
		pointer = self.head_value
		count += 1
		while self.circle[pointer].prev != self.head_value:
			pointer = self.circle[pointer].prev
			count += 1
		print("count backward = " + str(count))		
		
def max_val_in_circle(c):
	return max(c.circle.keys())

list = LList()

for i in [3,2,7,4,6,5,1,8,9]:
#for i in [3,8,9,1,2,5,4,6,7]:
	list.append(Cup(i))

	
for i in range(10,1000001):
	list.append(Cup(i))

list.link_ends()
#list.print_list()

current = list.retrieve(3)
print("loaded list")
for i in range(10000000):
	if i % 10000 == 0:
		print(str(i))
	sublist = []
	
	#extract 3 cups
	for j in range(3):
		sublist.append(list.extract(current.next))
	
	search_target = current.val-1
	target_cup = list.retrieve(search_target)
	while target_cup == None:
		search_target -= 1
		if search_target < 1:
			search_target = max_val_in_circle(list)
		target_cup = list.retrieve(search_target)
	
	list.insert_after(target_cup,sublist[0])
	list.insert_after(sublist[0],sublist[1])
	list.insert_after(sublist[1],sublist[2])
		
	#list.print_list()
	#list.check_consistency()
	
	current = list.retrieve(current.next)
	
ind = list.retrieve(1)
next = list.retrieve(ind.next)
next2 = list.retrieve(next.next)
		
result = next.val * next2.val
print(result)
	
