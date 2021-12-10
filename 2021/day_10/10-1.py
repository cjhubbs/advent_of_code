def validate(l):
  opening = "([{<"
  closing = ")]}>"
  matching_open = {")": "(", "}": "{", "]": "[", ">": "<"}
  stack = []
  for c in l:
    if c in opening:
      stack.append(c)
    else:
      if stack[-1] == matching_open[c]:
        stack.pop()
      else:
        return c 
  return -1
  

f = open("input10.txt","r")

score = 0
for line in f.readlines():
  result = validate(line.strip())
  if result == ")":
    score += 3
  elif result == "]":
    score += 57
  elif result == "}":
    score += 1197
  elif result == ">":
    score += 25137
    
    
print("score is:", score)
