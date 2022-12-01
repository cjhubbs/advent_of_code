class FoodParser():
  def __init__(self, filename):
    self.filename = filename
    self.cal_list = []
  
  def parse(self):
    with open(self.filename) as f:
      lines = f.read().splitlines()
    
    current_sum = 0
    for l in lines:
      if l == "":
        self.cal_list.append(current_sum)
        current_sum = 0
      else:
        current_sum += int(l)
    
    self.cal_list.sort(reverse=True)
        
  def get_max_calories(self):
    return self.cal_list[0]
  
  def get_sum_of_top_three(self):
    return self.cal_list[0]+self.cal_list[1]+self.cal_list[2]

if __name__ == "__main__":
  
  fp = FoodParser('1-input.txt')
  fp.parse()
  
  print("Part 1: Max calories is ", fp.get_max_calories())   
  print("Part 2: Sum of 3 greatest is ", fp.get_sum_of_top_three())
