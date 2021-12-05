f = open("input6.txt", "r")
found_chars = {}
total_count = 0
group_count = 0

for x in f: 
	if x == "\n":
		for key in found_chars:
			if found_chars[key] == group_count:
				total_count += 1
		found_chars = {}
		group_count = 0
	else:
		group_count += 1
		for c in x.strip():
			if c in found_chars:
				found_chars[c] += 1
			else:
				found_chars[c] = 1

print(str(total_count))
