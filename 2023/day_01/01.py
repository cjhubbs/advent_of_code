class CalibrationDoc():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    self.names = ['_','one','two','three','four','five','six','seven','eight','nine']
    self.names_reversed = ['_','eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']
  
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
          s = reversed_line[i:i+len(self.names_reversed[d])]
          if s == self.names_reversed[d]:
            return d 
            
  def assemble_first_last_number(self,line,accept_names):
    first = self.get_first_digit(line,accept_names)
    second = self.get_last_digit(line,accept_names)
    num = int(str(first) + str(second))
    return num      

  def sum_numbers(self,accept_names):
    sum = 0
    for l in self.lines:
      sum += self.assemble_first_last_number(l,accept_names)
    return sum


if __name__ == "__main__":
  
  cd = CalibrationDoc('01_input.txt')
  #cd = CalibrationDoc('01_test.txt')
  cd.parse()
  print("Part 1: ", cd.sum_numbers(False))
  print("Part 2: ", cd.sum_numbers(True))

