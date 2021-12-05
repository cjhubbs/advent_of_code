f = open("input6.txt", "r")
max_id = 0
found_chars = {}
total_count = 0

for x in f: 
	if x == "\n":
		print(found_chars)
		total_count += len(found_chars)
		found_chars = {}
	else:
		print(x)
		for c in x.strip():
			print(c)
			found_chars[c] = 1

print(str(total_count))
