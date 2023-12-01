class CalibrationDoc():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    self.names = ['_','one','two','three','four','five','six','seven','eight','nine']
    self.names_reversed = ['_','eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']
  
  def parse(self):
    with open(self.filename) as f:
      self.lines = f.read().splitlines()

  def get_digit(self,line,accept_names,names):
    for i in range(len(line)):
      if line[i].isdigit():
        return line[i]
      elif accept_names:
        for d in range(len(names)):
          s = line[i:i+len(names[d])]
          if s == names[d]:
            return d 

  def assemble_first_last_number(self,line,accept_names):
    first = self.get_digit(line,accept_names,self.names)
    second = self.get_digit(line[::-1],accept_names,self.names_reversed)
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

