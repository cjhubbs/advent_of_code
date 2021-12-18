import itertools

def parse_line(l):
  tokens = []
  temp = ""
  for char in l:
    if char == "[":
      tokens.append(char)
    elif char in "],":
      if temp:
        tokens.append(int(temp))
        temp = ""
      tokens.append(char)
    elif char.isdigit():
      temp += char
  return tokens

def add_numbers(first,second):
  result = ['[']
  for token in first:
    result.append(token)
  result.append(',')
  for token in second:
    result.append(token)
  result.append(']')
  return result

def explode(n):
  last_int_index = -1
  depth_count = 0
  x = []
  for idx, token in enumerate(n):
    if isinstance(token, int):
      last_int_index = idx 
    elif token == "[":
      depth_count += 1
    elif token == "]":
      depth_count -= 1
    
    if depth_count == 5:
      #explode
      left_num = n[idx+1]
      right_num = n[idx+3]
      
      #add left number to digit to left
      if last_int_index > -1:
        x[last_int_index] = x[last_int_index] + left_num
      
      #add right number to digit to right
      for temp_idx in range(idx+4,len(n)):
        if isinstance(n[temp_idx],int):
          n[temp_idx] = n[temp_idx] + right_num
          break
      
      #add in a zero
      x.append(0)
      
      # skip the open bracket, the two ints, the comma, and the close bracket
      # append the rest of the string, only take one action at a time
      for temp_idx in range(idx+5,len(n)):
        x.append(n[temp_idx])
      return x
    
    x.append(token)  
  
  return x

def split_num(n):
  x = []
  for idx, token in enumerate(n):
    if isinstance(token,int):
      if token > 9:
        left = token // 2
        right = (token + 1) // 2
        x.append("[")
        x.append(left)
        x.append(",")
        x.append(right)
        x.append("]")
        for tmp_idx in range(idx+1,len(n)):
          x.append(n[tmp_idx])
        return x
      else:
        x.append(token)
    else:
      x.append(token)
  return x

def reduce(n):
  new_n = explode(n)
  if new_n == n:
    new_n = split_num(n)
  return new_n

def reduce_fully(n):
  cur_n = n[:]
  new_n = reduce(cur_n)
  while cur_n != new_n:
    cur_n = new_n[:]
    new_n = reduce(cur_n)
  return new_n    
  
def magnitude(n):
  
  # stack the ints as you encounter them. When you hit a right bracket, 
  # do the math on the last two ints and re-stack the result
  num_stack = []
  for token in n:
    if isinstance(token,int):
      num_stack.append(token)
    if token == "]":
      r = num_stack.pop()
      l = num_stack.pop()
      tmp = l*3 + r*2
      num_stack.append(tmp)
  return num_stack[0]  
    
f = open("input18.txt","r")

numbers = []
p2n = []
for line in f.readlines():
  numbers.append(parse_line(line.strip()))
p2n = numbers[:]

n = numbers[0]  
for next_num in range(1,len(numbers)):
  n = reduce_fully(add_numbers(n,numbers[next_num]))

print("p1 magnitude is", magnitude(n))

max = 0

for i in range(len(p2n)):
  for j in range(len(p2n)):
    if i != j:
      mag = magnitude(reduce_fully(add_numbers(p2n[i],p2n[j])))
      if mag > max:
        max = mag 
print("p2 max is",max)
