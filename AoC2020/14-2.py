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

def write_to_memory(new_addr,addr,mask,val):
	global memory
	if len(new_addr) == 36:
		memory["".join(new_addr)] = val
	else:
		tmp_list = new_addr
		index = len(tmp_list)
		while index < 36 and mask[index] != "X":
			if mask[index] == '0':
				tmp_list.append(addr[index])
			else:
				tmp_list.append('1')
			index += 1
		if index == 36:
			memory["".join(tmp_list)] = val 
		else:
			list_for_0 = tmp_list + ["0"]
			list_for_1 = tmp_list + ["1"]
			write_to_memory(list_for_0,addr,mask,val)
			write_to_memory(list_for_1,addr,mask,val)
""
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
		addr = dec_to_bin_string(int(mem.group(1)))
		new_addr = []
		write_to_memory(new_addr,addr,current_mask,int(mem.group(2)))

print(sum(memory.values()))
