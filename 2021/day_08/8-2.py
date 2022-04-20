f = open("input8.txt", "r")
data = f.readlines()
parts = [x.strip().split("|") for x in data]

temp_inputs = []
temp_outputs = []
sorted_inputs = []
sorted_outputs = []
for x in parts:
  temp_inputs.append(x[0].split())
  temp_outputs.append(x[1].split())
  
for x in temp_inputs:
  r = []
  for y in x:
    y = "".join(sorted(y))
    r.append(y)
  sorted_inputs.append(r)

for x in temp_outputs:
  r = []
  for y in x:
    y = "".join(sorted(y))
    r.append(y)
  sorted_outputs.append(r)
  
grand_total = 0

for idx in range(len(sorted_inputs)):
  s = sorted_inputs[idx]
  
  k = ["","","","","","","","","abcdefg",""]
  
  #these are the easy ones
  for i in s:
    if len(i) == 2:
      k[1] = i 
    if len(i) == 3:
      k[7] = i 
    if len(i) == 4:
      k[4] = i 

  ell = k[4]
  for c in k[1]:
    ell = ell.replace(c,'')

  for i in s:
    #if strlen = 5 and incl both segments from 1, digit = 3
    if len(i) == 5:
      found = True
      for c in k[1]:
        found = found and c in i 
      if found:
        k[3] = i
        
      #if strlen == 5 and incl both segments from the ell, digit = 5
      found = True
      for c in ell:
        found = found and c in i 
      if found:
        k[5] = i 
      
      if not (i == k[3] or i == k[5]):
        k[2] = i 

    if len(i) == 6:
      #if incl all of digit 4, digit == 9
      found = True
      for c in k[4]:
        found = found and c in i 
      if found:
        k[9] = i 
      
      #if not incl both segments of digit 1, digit == 6
      if not (k[1][0] in i and k[1][1] in i):
        k[6] = i
      
      if not (i == k[6] or i == k[9]):
        k[0] = i

  digits = []
  for o in sorted_outputs[idx]:
    digits.append(k.index(o))
  val = 1000*digits[0] + 100*digits[1] + 10*digits[2] + digits[3]
  grand_total += val 

print("grand total is ", grand_total)
