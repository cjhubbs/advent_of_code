def filter_list(l, pos, char):
  ret_list = []
  for item in l:
    if item[pos] == char:
      ret_list.append(item)
  return ret_list

def get_filter_char(l,pos,most_least,default):
  other = ["1","0"]
  count = 0
  for item in l:
    if item[pos] == default:
      count += 1
  if most_least == "most":
    if count >= (len(l) / 2):
      return default
    else:
      return other[int(default)]
  else:
    if count <= (len(l) / 2):
      return default
    else:
      return other[int(default)]

def b_to_d(bin_str):
  ret_val = 0
  weight = 1
  for i in reversed(range(len(bin_str))):
    if bin_str[i] == "1":
      ret_val += weight
    weight = weight * 2
  return ret_val

width = 12

oxy_list = [line.rstrip() for line in open('input3.txt')]
co2_list = oxy_list[:]

for pos in range(width):
  keep_digit = get_filter_char(oxy_list,pos,"most","1")
  keep_oxy = filter_list(oxy_list,pos,keep_digit)
  oxy_list = keep_oxy[:]
  if len(oxy_list) == 1:
    break

for pos in range(width):
  keep_digit = get_filter_char(co2_list,pos,"least","0")
  keep_co2 = filter_list(co2_list,pos,keep_digit)
  co2_list = keep_co2[:]
  if len(co2_list) == 1:
    break
    
oxy = b_to_d(oxy_list[0])
co2 = b_to_d(co2_list[0])
  
print("oxy is " + str(oxy))
print("co2 is " + str(co2))
print("Product is " + str(oxy*co2))
