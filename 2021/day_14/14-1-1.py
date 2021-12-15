from collections import Counter

subs = {}  

def update_counts(counts):
  new_counts = {}
  for key, val in counts.items():
    if subs[key][0] in new_counts.keys():
      new_counts[subs[key][0]] += val 
    else:
      new_counts[subs[key][0]] = val 
    if subs[key][1] in new_counts.keys():
      new_counts[subs[key][1]] += val   
    else:
      new_counts[subs[key][1]] = val
  return new_counts
    

pairs = {}
f = open("input14.txt","r")
data = f.readlines()
start_string = data.pop(0).strip()
for i in range(len(start_string)-1):
  p = start_string[i:i+2]
  if p in pairs.keys():
    pairs[p] += 1
  else:
    pairs[p] = 1


for l in data:
  substr = []
  d = l.strip().split(" -> ")
  first_new_pair = d[0][0] + d[1]
  second_new_pair = d[1] + d[0][1]
  substr.append(first_new_pair)
  substr.append(second_new_pair)
  subs[d[0]] = substr

steps = 40
for i in range(steps):
  pairs = update_counts(pairs)

char_counts = {}
for key,val in pairs.items():
  if key[0] in char_counts.keys():
    char_counts[key[0]] += val
  else:
    char_counts[key[0]] = val
  if key[1] in char_counts.keys():
    char_counts[key[1]] += val
  else:
    char_counts[key[1]] = val
char_counts[start_string[0]] += 1
char_counts[start_string[-1]] += 1 

sorted_counts = dict(sorted(char_counts.items(), key=lambda item: item[1]))

diff = int(list(sorted_counts.items())[-1][1]) - int(list(sorted_counts.items())[0][1])
print("diff is", diff / 2)
