import numpy as np

def list_of_bingo_indices(pile):
  indices = []
  for idx, card in enumerate(pile):
    col_bingo = card.sum(axis=0).max() == 5
    row_bingo = card.sum(axis=1).max() == 5
    if (col_bingo or row_bingo):
      indices.append(idx) 
  return indices
  
def calculate_value(cards,drawn,idx,last_num):
  sum = 0
  print(drawn[idx])
  for x in range(5):
    for y in range(5):
      if drawn[idx][x][y] == 0:
        sum += cards[idx][x][y]
  return (sum*last_num)

input_data = [line.rstrip() for line in open('input4.txt')]
num_of_cards = int((len(input_data) - 1) / 6)

calls = input_data.pop(0).split(",")

cards = np.zeros((num_of_cards,5,5),dtype=int)
drawn = np.zeros((num_of_cards,5,5),dtype=int)

#load the cards
cur_card = 0
cur_row = 0
while(input_data):
  line = input_data.pop(0)
  if line:
    row = [int(x) for x in line.split()]
    cards[cur_card][cur_row] = row 
    cur_row += 1 
    if cur_row == 5:
      cur_card += 1
      cur_row = 0

for num in calls:
  result = np.where(cards==int(num))
  found = list(zip(result[0],result[1],result[2]))
  
  for i in found:
    drawn[i] = 1
  winning_indices = list_of_bingo_indices(drawn)
  if len(winning_indices) == 1:
    p1_value = calculate_value(cards, drawn, winning_indices[0],int(num))
    print("Part 1 value is " + str(p1_value))
  unwon_card = -1
  if len(winning_indices) == num_of_cards-1:
    for i in range(num_of_cards):
      if winning_indices[i] != i:
        last_card = i
        break
  if len(winning_indices) == num_of_cards:  
    p2_value = calculate_value(cards, drawn, last_card,int(num))
    print("Part 2 value is " + str(p2_value))
    break
