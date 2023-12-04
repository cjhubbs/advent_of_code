class Number():
  def __init__(self,val,row,start,end):
    self.val = val
    self.r = row 
    self.s = start 
    self.e = end 
  
  def value(self):
    return self.val 
  def row(self):
    return self.r 
  def start(self):
    return self.s 
  def end(self):
    return self.e 
  
  def is_adjacent_to_point(self,row,col):
    adj = False
    if row == self.r and ((col == self.s - 1) or (col == self.e+1)):
      adj = True 
    if row == self.r-1 or row == self.r+1:
      if col >= self.s-1 and col <= self.e+1:
        adj = True 
    return adj 

class Schematic():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    with open(self.filename) as f:
      self.lines = f.read().splitlines()

  def get_numbers_in_line(self,l,row):
    in_number = False
    num_string = ''
    start = -1
    end = -1
    numbers = []
    for i in range(len(l)):
      if l[i].isdigit():
        num_string += l[i]
        if not in_number:
          in_number = True
          start = i
      else:
        if in_number:
          end = i-1 
          numbers.append(Number(int(num_string),row,start,end))
          start = -1
          end = -1
          in_number = False
          num_string = ''
    if in_number:
      end = i-1
      numbers.append(Number(int(num_string),row,start,end))
    return numbers   
  
  def number_is_adjacent_to_symbol(self,n):
    row_min = n.row()-1
    row_max = n.row()+1
    col_min = n.start()-1
    col_max = n.end()+1
    for r in range(row_min,row_max+1):
      for c in range(col_min,col_max+1):
        if r >= 0 and r < len(self.lines):
          if c >= 0 and c < len(self.lines[0]):
            if (not self.lines[r][c].isdigit()) and (not self.lines[r][c] == "."):
              return True
    return False             
  
  def get_gear_points(self):
    points = []
    for l in range(len(self.lines)):
      for c in range(len(self.lines[0])):
        if self.lines[l][c] == "*":
          points.append({'row': l,'col':c})
    return points
  
  def is_adjacent_to_two_numbers(self,nums, p):
    adjacent = []
    for n in nums:
      if n.is_adjacent_to_point(p['row'],p['col']):
        adjacent.append(n.value())
    if len(adjacent) == 2:
      return adjacent[0],adjacent[1]
    else:
      return 0,0

  
if __name__ == "__main__":
  
  s = Schematic('03-input.txt')
  sum = 0
  all_nums = []

  for r in range(len(s.lines)):
    nums = s.get_numbers_in_line(s.lines[r],r)
    all_nums.extend(nums)
    for n in nums:
      if s.number_is_adjacent_to_symbol(n):
        sum += n.value()
  print(sum)

  total_gear_ratio = 0
  gear_points = s.get_gear_points()
  for p in gear_points:
    g1, g2 = s.is_adjacent_to_two_numbers(all_nums, p)
    total_gear_ratio += (g1*g2)
  print(total_gear_ratio)