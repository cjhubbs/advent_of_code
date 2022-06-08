children = {}
parent = {}
depth = {}
orbits = 0

def get_path_to(root,target):
  global parent
  path = []
  current = target
  while current != root:
    path.append(current)
    current = parent[current]
  return path 

def stack_traverse(node):
  global children
  global orbits
  global depth
  global parent
  current = node
  stack = []
  children_have_been_stacked = []
  stack.append(node)
  while len(stack) > 0:
    current = stack[-1]
    if current not in children_have_been_stacked:
      if current in children.keys():
        for c in children[current]:
          stack.append(c)
          depth[c] = depth[current] + 1
        children_have_been_stacked.append(current)
      else:
        orbits += depth[current]
        stack.pop()
    else:
      orbits += depth[current]
      stack.pop()
      
f = open("input6.txt", "r")
for x in f:
  p,c = x.strip().split(")")
  if p not in children.keys():
    children[p] = []
  children[p].append(c) 
  parent[c] = p

depth["COM"] = 0
stack_traverse("COM")
print("p1 orbits: ",orbits)

#part 2

#get paths too YOU and to SAN; easy when going from target back to root
path1 = get_path_to("COM","YOU")
path2 = get_path_to("COM","SAN")

#reverse so you have root-to-target path
path1.reverse()
path2.reverse()
distance = 0

#worst case is only common node is root, subtract 2 to eliminate target nodes
total_length = len(path1) + len(path2) - 2

#for every step from root that is common, subtract those nodes
for i in range(min(len(path1),len(path2))):
  if path1[i] == path2[i]:
    total_length -= 2
  else:
    break

print("p2 xfers required = ",total_length)
