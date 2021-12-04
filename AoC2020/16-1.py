from collections import namedtuple
import re 

ValidRange = namedtuple('ValidRange','min max')

class Field:
	def __init__(self,name,r1l, r1h,r2l,r2h):
		self.name = name
		self.range1 = ValidRange(int(r1l),int(r1h))
		self.range2 = ValidRange(int(r2l),int(r2h))
		
	def ValueInRange(self,val):
		return (val >= self.range1.min and val <= self.range1.max) or (val >= self.range2.min and val <= self.range2.max)
	

f = open("input16.txt","r")
data = f.read().splitlines()
f.close()

fields = []
your_ticket_next = 0
other_tickets_next = 0
your_ticket = []
nearby_tickets = []

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
		
print(your_ticket)
print(nearby_tickets)
print(fields)

sum_invalid = 0

for t in nearby_tickets:
	for val in t:
		valid = 0
		for f in fields:
			if f.ValueInRange(int(val)):
				valid = 1
				break
		if not valid:
			sum_invalid += int(val)

print(sum_invalid)
			
	
