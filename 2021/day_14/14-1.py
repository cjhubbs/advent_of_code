from collections import Counter

subs = {}  

def do_insertions(s):
  new_str = ""
  for i in range(len(s)-1):
    new_str += s[i]
    c = s[i:i+2]
    if c in subs.keys():
      new_str += subs[c]
  new_str += s[-1]
  return new_str

f = open("input14.txt","r")
data = f.readlines()
string = data.pop(0).strip()

for l in data:
  d = l.strip().split(" -> ")
  subs[d[0]] = d[1]

steps = 40
for i in range(steps):
  string = do_insertions(string)
  print("finished step", i)
  print('length is',len(string))

counts = Counter(string)
sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1]))
diff = int(list(sorted_counts.items())[-1][1]) - int(list(sorted_counts.items())[0][1])
print("diff is", diff)
