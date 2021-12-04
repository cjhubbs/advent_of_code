def is_operator(s):
	return s == -8 or s == -7
def is_digit(s):
	return s >= 0 and s <= 9
def is_digit_char(s):
	return s == "1" or s == "2" or s =="3" or s=="4" or s=="5" or s=="6" or s=="7" or s=="8" or s=="9"
def is_number(s):
	return s >= 0

def process_operand(op1,op2,a):
	if a == -8:
		return (op1 * op2)
	elif a == -7:
		return (op1 + op2)
	else:
		return -1	

# ( = -10
# ) = -9
# * = -8
# + = -7

f = open("input18.txt","r")
data = f.read().splitlines()
f.close()

total = 0

for d in data:
	tokens = []
	stack = []
	for c in range(len(d)):
		if d[c] != " ":
			tokens.append(str(d[c]))
			
	print(tokens)
	for i in range(0,len(tokens)):
		if is_digit_char(tokens[i]):
			stack.append(int(tokens[i]))
		elif tokens[i] == '(':
			stack.append(-10)
		elif tokens[i] == ')':
			stack.append(-9)
		elif tokens[i] == '*':
			stack.append(-8)
		elif tokens[i] == '+':
			stack.append(-7)
		
		while (stack[-1] != -10 and stack[-1] != -8 and stack[-1] != -7 and len(stack)>2):
			if is_number(stack[-1]) and is_number(stack[-3]) and is_operator(stack[-2]):
				op1 = stack.pop()
				action = stack.pop()
				op2 = stack.pop()
				stack.append(process_operand(op1,op2,action))				
			elif stack[-3] == -10 and is_number(stack[-2]) and stack[-1] == -9:
				trash = stack.pop()
				tmp = stack.pop()
				trash2 = stack.pop()
				stack.append(tmp)
			else:
				break
	print(stack)
	total += stack[0]
	
print(total)
