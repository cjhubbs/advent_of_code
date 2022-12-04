class cleaning:
  def __init__(self, line):
    [t1, t2] = line.split(",")
    self.a1 = [int(i) for i in t1.split("-")]
    self.a2 = [int(i) for i in t2.split("-")]  

  def has_full_overlap(self):
    return ((self.a1[0] <= self.a2[0] and self.a1[1] >= self.a2[1]) or 
           (self.a2[0] <= self.a1[0] and self.a2[1] >= self.a1[1]))

  def has_any_overlap(self):
    if self.a1[0] < self.a2[0] and self.a1[1] < self.a2[0]:
      return False
    elif self.a2[0] < self.a1[0] and self.a2[1] < self.a1[0]:
      return False
    else:
      return True

if __name__ == "__main__":
  
  p1_count = 0
  p2_count = 0
  
  with open('4-input.txt') as f:
    lines = f.read().splitlines()
  for l in lines:
    c = cleaning(l)
    if c.has_full_overlap():
      p1_count += 1
    if c.has_any_overlap():
      p2_count += 1 
  
  print(p1_count, " assignments have full overlap")
  print(p2_count, " assignments have some overlap")
