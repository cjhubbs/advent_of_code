import math

def parse_line(l):
  tokens = []
  temp = ""
  for char in l:
    if char == "[":
      tokens.append(char)
    elif char in "],":
      if temp:
        tokens.append(temp)
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
    if token.isdigit():
      last_int_index = idx 
    elif token == "[":
      depth_count += 1
    elif token == "]":
      depth_count -= 1
    
    if depth_count == 5:
      #explode
      left_num = int(n[idx+1])
      right_num = int(n[idx+3])
      
      #add left number to digit to left
      if last_int_index > -1:
        x[last_int_index] = str(int(x[last_int_index]) + left_num)
      
      #add right number to digit to right
      for temp_idx in range(idx+4,len(n)):
        if n[temp_idx].isdigit():
          n[temp_idx] = str(int(n[temp_idx]) + right_num)
          break
      
      #add in a zero
      x.append("0")
      
      #discard the open bracket, the two digits, the comma, and the close bracket
      # append the rest of the string, only take one action at a time
      for temp_idx in range(idx+5,len(n)):
        x.append(n[temp_idx])
      return x
    
    x.append(token)  
  
  return x

def split_num(n):
  x = []
  for idx, token in enumerate(n):
    if token.isdigit():
      int_t = int(token)
      if int_t > 9:
        left = str(int(math.floor(int_t / 2)))
        right = str(int(math.ceil(int_t / 2)))
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
  
def calc_magnitude(n):
  num_stack = []
  for token in n:
    if token.isdigit():
      num_stack.append(int(token))
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
  n = add_numbers(n,numbers[next_num])
  n = reduce_fully(n)    

print("p1 magnitude is", calc_magnitude(n))

max = 0
for i in range(len(p2n)):
  for j in range(len(p2n)):
    if i != j:
      s = add_numbers(p2n[i],p2n[j])
      s = reduce_fully(s)
      mag = calc_magnitude(s)
      if mag > max:
        max = mag 
print("p2 max is",max)
