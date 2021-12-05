import re 
bit_val = []

def dec_to_bin_string(num):
	out = "000000000000000000000000000000000000"
	l = list(out)
	for i in range(36):
		if num >= bit_val[i]:
			l[i] = '1'
			num -= bit_val[i]
	return "".join(l)

def bin_string_to_dec(num):
	out_val = 0
	for i in range(36):
		if num[i] == '1':
			out_val += bit_val[i]
	return out_val

def apply_mask(num,mask):
	out_l = []
	for i in range(36):
		if mask[i] == 'X':
			out_l.append(num[i])
		elif mask[i] == '1':
		  out_l.append('1')
		else:	
			out_l.append('0')
	return "".join(out_l)

for i in range(35,-1,-1):
	bit_val.append(2**i)

f = open("input14.txt","r")
data = f.read().splitlines()
f.close()

memory = {}
current_mask = ""

for d in data:
	mask = re.search('mask = (\w{36})',d)
	mem = re.search('mem\[(\d+)\] = (\d+)',d)
	if mask:
		current_mask = mask.group(1)
	elif mem:
		memory[mem.group(1)] = bin_string_to_dec(apply_mask(dec_to_bin_string(int(mem.group(2))),current_mask))

print(memory)
print(sum(memory.values()))
