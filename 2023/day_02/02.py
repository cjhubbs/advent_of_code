class Game():
  def __init__(self, filename):
    self.filename = filename
    self.lines = []
    self.max = {'red': 12,'green': 13,'blue': 14}
    with open(self.filename) as f:
      self.lines = f.read().splitlines()
      
  def check_game_possible(self,l):
    self.max = {'red': 12,'green': 13,'blue': 14}
    pieces = l.split(':')
    id = int(pieces[0].split(' ')[1])
    plays = pieces[1].split(';')
    possible = True 
    
    for p in plays:
      dice = p.split(',')
      for d in dice:
        clean = d.strip()
        parts = clean.split(' ')
        if int(parts[0]) > self.max[parts[1]]:
          possible = False
    if possible:
      return int(id) 
    else:
      return 0    
      
  def calc_game_power(self,l):
    self.max = {'red': 0,'green': 0,'blue': 0}
    pieces = l.split(':')
    id = int(pieces[0].split(' ')[1])
    plays = pieces[1].split(';')
    
    for p in plays:
      dice = p.split(',')
      for d in dice:
        parts = d.strip().split(' ')
        self.max[parts[1]] = max(self.max[parts[1]],int(parts[0]))
    
    return self.max['red']*self.max['green']*self.max['blue']

if __name__ == "__main__":
  
  #g = Game('02-test.txt')
  g = Game('02-input.txt')
  sum = 0

  for l in g.lines:
    sum += g.check_game_possible(l)
  print(sum)
  
  sum = 0
  for l in g.lines:
    sum += g.calc_game_power(l)
  print(sum)
