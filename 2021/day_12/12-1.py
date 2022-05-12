nodes = {}
paths = {}


def log_path(p):
  t = "".join(p) + ",end"
  if t in paths.keys():
    paths[t] += 1
  else:
    paths[t] = 1

def traverse(path):
  node = path[-1]
  for n in nodes[node]:
    if n == 'end':
      log_path(path)   
    elif path.count(n) == 0 or n.isupper():
      path.append(n)
      traverse(path) 
               
  path.pop(-1)
  return

f = open("input12.txt", "r")
for line in f:
  p = line.strip().split("-")
  if p[0] in nodes.keys():
    nodes[p[0]].append(p[1])
  else:
    nodes[p[0]] = [p[1]]
  if p[1] in nodes.keys():
    nodes[p[1]].append(p[0])
  else:
    nodes[p[1]] = [p[0]]

print(nodes)
path = [ 'start' ]


traverse(path)
  
print(len(paths.keys()))
