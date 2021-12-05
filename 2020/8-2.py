import re 

original_instr = []
modified_instr = []
values = []
executed = []
swap_index = 0
acc = 0
pc = 0

def reset_instructions():
	global pc
	global acc
	for i in range(0,len(original_instr)-1):
		modified_instr[i] = original_instr[i]
		executed[i] = 0
		pc = 0
		acc = 0
		
def find_next_swap():
	global swap_index
	while modified_instr[swap_index] == 'acc':
		swap_index += 1
	if modified_instr[swap_index] == 'nop':
		modified_instr[swap_index] = 'jmp'
		swap_index += 1
	else:
		modified_instr[swap_index] = 'nop'
		swap_index += 1

pattern = '^([\w]{3}) ([+-]\d{1,3})$'
p = re.compile(pattern)

f = open("input8.txt", "r")
for l in f:
	stuff = p.search(l)
	original_instr.append(stuff.group(1))
	modified_instr.append(stuff.group(1))
	values.append(int(stuff.group(2)))
	executed.append(0)

found_it = 0
while found_it == 0:
	reset_instructions()
	find_next_swap()
	while executed[pc] == 0 and pc != len(original_instr):
		executed[pc] = 1
		if modified_instr[pc] == "acc":
			acc += values[pc]
			pc += 1
		elif modified_instr[pc] == "nop":
			pc += 1
		elif modified_instr[pc] == "jmp":
			pc += values[pc]
	if pc == len(original_instr):
		found_it = 1
		
	print("pc  = " + str(pc))	
	print("acc = " + str(acc))
	
