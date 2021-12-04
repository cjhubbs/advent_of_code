class Numrec:
	def __init__(self,index):
		self.count = 1
		self.cur_index = index
		self.prev_index = -1
	
	def AddIndex(self,index):
		self.count += 1
		self.prev_index = self.cur_index
		self.cur_index = index
	
n = [1,0,18,10,19,6]
recs = {}
for i in range(len(n)):
	recs[str(n[i])] = Numrec(i)

i = len(n)
prev_rec = recs[str(n[i-1])]
#limit = 2020
limit = 30000000

while i < limit:
	num_to_use = 0
	
	if prev_rec.count > 1:
		num_to_use = (i - prev_rec.prev_index)-1 
	
	s_to_use = str(num_to_use)
	if s_to_use in recs:
		recs[s_to_use].AddIndex(i)
	else:
		recs[s_to_use] = Numrec(i)

	n.append(num_to_use)
	prev_rec = recs[s_to_use]
	i += 1
	
print(n[limit-1])
