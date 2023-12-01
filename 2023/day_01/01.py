class CalibrationDoc():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    self.names = ['xxxxxxxxxxxxxxxxxxx','one','two','three','four','five','six','seven','eight','nine']
    self.names_reversed = ['xxxxxxxxxxxxxxxxxxx','eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']
  
  def parse(self):
    with open(self.filename) as f:
      self.lines = f.read().splitlines()

  def get_first_digit(self,line,accept_names):
    for i in range(len(line)):
      if line[i].isdigit():
        return line[i]
      elif accept_names:
        for d in range(len(self.names)):
          if line[i:i+len(self.names[d])] == self.names[d]:
            return d 

  def get_last_digit(self,line,accept_names):
    reversed_line = line[::-1]
    for i in range(len(line)):
      if reversed_line[i].isdigit():
        return reversed_line[i]
      elif accept_names:
        for d in range(len(self.names)):
          if line[i:i+len(self.names[d])] == self.names_reversed[d]:
            return d 
            
  def assemble_first_last_number(self,line,accept_names):
    first = self.get_first_digit(line,accept_names)
    second = self.get_last_digit(line,accept_names)
    num = int(str(first) + str(second))
    return num      

if __name__ == "__main__":
  
  #cd = CalibrationDoc('01_input.txt')
  cd = CalibrationDoc('01_test.txt')
  cd.parse()
  sum = 0
  for l in cd.lines:
    sum += cd.assemble_first_last_number(l,False)
  print(sum)
  
  sum = 0
  for l in cd.lines:
    sum += cd.assemble_first_last_number(l,True)
  print(sum)
