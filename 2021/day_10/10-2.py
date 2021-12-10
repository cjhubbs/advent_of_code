def get_completion(l):
  opening = "([{<"
  closing = ")]}>"
  matching_open = {")": "(", "}": "{", "]": "[", ">": "<"}
  matching_close = {"(": ")", "{": "}", "[": "]", "<": ">"} 
  stack = []
  for c in l:
    if c in opening:
      stack.append(c)
    else:
      if stack[-1] == matching_open[c]:
        stack.pop()
      else:
        return 0 
  #if we get here the line is valid, just incomplete
  completion = []
  while stack:
    completion.append(matching_close[stack.pop()])
  return completion 
  

f = open("input10.txt","r")

points = { ")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in f.readlines():
  val = get_completion(line.strip())
  if val:
    score = 0
    for v in val:
      score = score * 5
      score = score + points[v]
    scores.append(score)
    
scores.sort()
idx = int(len(scores) // 2)
print("final val is:", scores[idx])
