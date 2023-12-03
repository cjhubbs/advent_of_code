class Schematic():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    with open(self.filename) as f:
      self.lines = f.read().splitlines()

  def get_numbers_in_line(self,l):
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
          numbers.append({'num': int(num_string),'start': start,'end':end})
          start = -1
          end = -1
          in_number = False
          num_string = ''
    return numbers   
  
  def is_adjacent_to_symbol(self,row,start,end):
    row_min = max(0,row-1)
    row_max = min(row+1,len(self.lines)+1)
    col_min = max(0,start-1)
    col_max = min(end+1,len(self.lines[0])+1%)
    for r in range(row_min,row_max):
      for c in range(col_min,col_max):
        if (not self.lines[r][c].isdigit()) and (not self.lines[r][c]) == ".":
          return True
    return False             
  
if __name__ == "__main__":
  
  s = Schematic('03-test.txt')
  #s = Schematic('03-input.txt')
  sum = 0

  for r in range(len(s.lines)):
    nums = s.get_numbers_in_line(s.lines[r])
    print(nums)
    for n in nums:
      if s.is_adjacent_to_symbol(r,n['start'],n['end']):
        sum += n['num']

  print(sum)
