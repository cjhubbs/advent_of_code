from collections import namedtuple

Tile = namedtuple("Tile","id,n,s,e,w")
edge_counts = {}
tiles = []

def count_single_edges(t):
	count = 0
	global edge_counts
	if edge_counts[t.n] == 1:
		count += 1
	if edge_counts[t.s] == 1:
		count += 1
	if edge_counts[t.e] == 1:
		count += 1
	if edge_counts[t.w] == 1:
		count += 1
	return count

f = open("input20.txt","r")
data = f.read().splitlines()
f.close()

tmp_tile = []
row_count = 0
for d in data:
	if "Tile" in d:
		tmp_id = d.split(" ")[1][0:4]
		row_count = 0
	elif d == "":
		pass
	else:
		tmp_tile.append(d)
		row_count += 1
	
	if row_count == 10:
		tmp_n = tmp_tile[0]
		tmp_s = tmp_tile[9]
		tmp_e = ""
		tmp_w = ""
		for i in range(10):
			tmp_w += tmp_tile[i][0]
			tmp_e += tmp_tile[i][9]
		tiles.append(Tile(tmp_id,tmp_n,tmp_s,tmp_e,tmp_w))
		tmp_tile = []
		row_count = 0

print(tiles)
for t in tiles:
	if t.n in edge_counts.keys():
		edge_counts[t.n] += 1
	else:
		edge_counts[t.n] = 1
	if t.s in edge_counts.keys():
		edge_counts[t.s] += 1
	else:
		edge_counts[t.s] = 1
	if t.e in edge_counts.keys():
		edge_counts[t.e] += 1
	else:
		edge_counts[t.e] = 1
	if t.w in edge_counts.keys():
		edge_counts[t.w] += 1
	else:
		edge_counts[t.w] = 1

result = 1		
print(edge_counts)
for t in tiles:
	if count_single_edges(t) == 2:
		result *= int(t.id)
print(result)
