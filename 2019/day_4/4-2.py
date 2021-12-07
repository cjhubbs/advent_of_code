start_num = 372037
end_num = 905157

match_count = 0

for n in range(start_num,end_num):
  invalid = False
  found_double = False 
  
  s = str(n)
  for i in range(1,len(s)):
    if s[i] < s[i-1]:
      invalid = True
    if s[i] == s[i-1]:
      num_of_char = s.count(s[i])
      if num_of_char == 2:
        found_double = True
  if (not invalid) and found_double:
    match_count += 1

print("Match count: ", match_count)
        
