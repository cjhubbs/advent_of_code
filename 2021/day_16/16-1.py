h2b = {"0": "0000", "1": "0001", "2":"0010","3":"0011","4":"0100","5":"0101", "6":"0110","7":"0111","8":"1000","9": "1001","A":"1010","B":"1011","C":"1100","D":"1101","E": "1110","F":"1111"}

def get_n_bits(n,bits):
  r = bits[:n]
  bits = bits[n:]
  return r,bits

def b2d(b):
  weight = 1
  v = 0
  for i in reversed(range(len(b))):
    if b[i] == "1":
      v += weight
    weight = weight * 2
  return v

def process_literal(bits):
  bin_string = ""
  read_another = 1
  while read_another:
    cont,bits = get_n_bits(1,bits)
    b,bits = get_n_bits(4,bits)
    bin_string += b
    if cont == "0":
      read_another = 0
  v = b2d(bin_string)
  return v,bits 

def process_operation(ptype, operands):
  if ptype == "000":
    v = sum(operands)
  elif ptype == "001":
    v = 1
    for i in operands:
      v = v * i
  elif ptype == "010":
    v = min(operands)
  elif ptype == "011":
    v = max(operands)
  elif ptype == "101":
    v = operands[0] > operands[1]
  elif ptype == "110":
    v = operands[0] < operands[1]
  elif ptype == "111":
    v = operands[0] == operands[1]
  return v 

def process_packet(bits):
  
  version,bits = get_n_bits(3,bits)
  ptype,bits = get_n_bits(3,bits)
  
  global version_sum
  version_sum += b2d(version)
  
  if ptype == "100":
    val,bits = process_literal(bits)
    return val, bits
  else:
    #operator packet
    length_type,bits = get_n_bits(1,bits)
    subp_vals = []
    if length_type == "0":
      len_string,bits = get_n_bits(15,bits)
      total_length_of_subpackets = b2d(len_string)
      subp,bits = get_n_bits(total_length_of_subpackets,bits)
      while subp:
        val, subp = process_packet(subp)
        subp_vals.append(val)      
    else:
      num_string,bits = get_n_bits(11,bits)
      num_of_subpackets = b2d(num_string)
      for i in range(num_of_subpackets):
        val, bits = process_packet(bits)
        subp_vals.append(val)
    
  v = process_operation(ptype,subp_vals)
    
  return v, bits

f = open("input16.txt","r")
hex_string = f.readline().strip()
#hex_string = "880086C3E88112"

bits = ""
ptr = 0
version_sum = 0

for h in hex_string:
  bits += h2b[h]

val, bits = process_packet(bits)
print("processed packet, remaining bits are:",bits)
print("version sum is",version_sum)
print("val is", val)
