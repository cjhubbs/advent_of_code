import re 

instr = []
values = []
executed = []

pattern = '^([\w]{3}) ([+-]\d{1,3})$'
p = re.compile(pattern)

acc = 0
pc = 0

f = open("input8.txt", "r")
for l in f:
	stuff = p.search(l)
	instr.append(stuff.group(1))
	values.append(int(stuff.group(2)))
	executed.append(0)

while executed[pc] == 0 and pc != len(instr):
	executed[pc] = 1
	if instr[pc] == "acc":
		acc += values[pc]
		pc += 1
	elif instr[pc] == "nop":
		pc += 1
	elif instr[pc] == "jmp":
		pc += values[pc]

print("pc  = " + str(pc))	
print("acc = " + str(acc))
	
