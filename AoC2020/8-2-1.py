instructions = []
swap_index = 0
acc = 0
pc = 0

class Instruction:

	def __init__(self, opcode, value):
		self.opcode = opcode
		self.value = int(value)
		self.modified_opcode = ""
		self.executed = 0
	
	def reset(self):
		self.modified_opcode = self.opcode
		self.executed = 0		
		
	def swapNopAndJmp(self):
		self.modified_opcode = 'jmp' if self.opcode == 'nop' else 'nop'

def find_next_swap():
	global swap_index
	while instructions[swap_index].modified_opcode == 'acc':
		swap_index += 1
	instructions[swap_index].swapNopAndJmp()
	swap_index += 1

data = open("input8.txt", "r").read().splitlines()
[instructions.append(Instruction(op,val)) for d in data for op,val in [d.split()]]

found_it = 0
while found_it == 0:
	[i.reset() for i in instructions]
	pc = 0
	acc = 0
	find_next_swap()
	
	while instructions[pc].executed == 0 and pc != len(instructions):
		instructions[pc].executed = 1
		if instructions[pc].modified_opcode == "acc":
			acc += instructions[pc].value
			pc += 1
		elif instructions[pc].modified_opcode == "nop":
			pc += 1
		elif instructions[pc].modified_opcode == "jmp":
			pc += instructions[pc].value
		if pc == len(instructions):
			found_it = 1
			break
	
print("pc  = " + str(pc))	
print("acc = " + str(acc))
	
