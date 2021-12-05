from collections import namedtuple
import re 

ValidRange = namedtuple('ValidRange','min max')

class Field:
	def __init__(self,name,r1l, r1h,r2l,r2h):
		self.name = name
		self.range1 = ValidRange(int(r1l),int(r1h))
		self.range2 = ValidRange(int(r2l),int(r2h))
		self.index = {}
		self.cannot_be = [0]*20
		
	def ValueInRange(self,val):
		return (val >= self.range1.min and val <= self.range1.max) or (val >= self.range2.min and val <= self.range2.max)
		
	def CannotBe(self,i):
		self.cannot_be[i] = 1	

f = open("input16.txt","r")
data = f.read().splitlines()
f.close()

fields = []
your_ticket_next = 0
other_tickets_next = 0
your_ticket = []
nearby_tickets = []
valid_tickets = []

for d in data:
	
	if your_ticket_next:
		your_ticket = d.split(',')
		your_ticket_next = 0
	if other_tickets_next:
		nearby_tickets.append(d.split(','))
	
	f = re.match('^([\w\s]+):\s(\d+)-(\d+) or (\d+)-(\d+)',d)
	if f:
		fields.append(Field(f.group(1),f.group(2),f.group(3),f.group(4),f.group(5)))
	
	yt = re.match('your ticket:',d)
	if yt:
		your_ticket_next = 1
	nt = re.match('nearby tickets:',d)
	if nt:
		other_tickets_next = 1
		
for t in nearby_tickets:
	ticket_valid = 1
	for val in t:
		field_valid = 0
		for f in fields:
			if f.ValueInRange(int(val)):
				field_valid = 1
				break
		if not field_valid:
			ticket_valid = 0
			break
	if ticket_valid:
		valid_tickets.append(t)

for vt in valid_tickets:
	c = 0
	for val in vt:
		for f in fields:
			if not f.ValueInRange(int(val)):
				f.CannotBe(c)
		c += 1
			
possibles = []

for i in range(20):
	di = {}
	for f in fields:
		if not f.cannot_be[i]:
			di[f.name] = 1
	possibles.append(di)
	
for k in range(20):
	for i in range(20):
		if len(possibles[i]) == 1:
			key = list(possibles[i].keys())[0]
			for j in range(20):
				if j != i:
					possibles[j].pop(key, None)

final_val = 1
for i in range(20):
	key = list(possibles[i].keys())[0]
	if re.match('^departure',key):
		final_val *= int(your_ticket[i])

print(final_val)
