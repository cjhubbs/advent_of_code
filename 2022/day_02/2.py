class rps:
  def __init__(self):
    self.transpose = { 'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
        
    self.part2_translate_result = { 'X': 'loss', 'Y': 'draw', 'Z': 'win'}
    self.part1_score = 0
    self.part2_score = 0

  def get_my_move(self, them, desired_outcome):
    if desired_outcome == 'draw':
      return them
    elif desired_outcome == 'win':
      if them == 'rock':
        return 'paper'
      elif them == 'paper':
        return 'scissors'
      else:
        return 'rock'
    else:
      if them == 'rock':
        return 'scissors'
      elif them == 'paper':
        return 'rock'
      else:
        return 'paper'
            
  def get_turn_points(self, move):
    if move == 'rock':
      return 1
    elif move == 'paper':
      return 2
    else:
      return 3
  
  def get_match_points(self, result):
    if result == 'win':
      return 6
    elif result == 'draw':
      return 3
    else:
      return 0  
  
  def get_match_result(self, them, me):
    if them == me: 
      return 'draw'
    else:
      if (them == 'rock' and me == 'paper') or (them == 'paper' and me == 'scissors') or (them == 'scissors' and me == 'rock'):
        return 'win'
      else:
        return 'loss'

if __name__ == "__main__":
   
  game = rps()
  with open('2-input.txt') as f:
    lines = f.read().splitlines()
  for l in lines:
    inputs = l.split()
    them = game.transpose[inputs[0]]
    me = game.transpose[inputs[1]]
    match_points = game.get_match_points(game.get_match_result(them, me))
    game.part1_score += match_points
    game.part1_score += game.get_turn_points(me)
    
    #part 2
    match_result = game.part2_translate_result[inputs[1]]
    match_points = game.get_match_points(match_result)
    my_move = game.get_my_move(them, match_result)
    turn_points = game.get_turn_points(my_move)
    game.part2_score += match_points 
    game.part2_score += turn_points    
    
  print("Part 1 total score is: ", game.part1_score)
  print("Part 2 total score is: ", game.part2_score)
  
