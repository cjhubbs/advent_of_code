from collections import namedtuple

Game = namedtuple("Game","hand0 hand1")

played_decks = {}
final_deck = []

def generate_history_key(d):
	tmp = ""
	for h in d:
		for c in h:
			tmp += str(c)
	return tmp
	
def store_deck_history(d):
	global played_decks	
	played_decks[generate_history_key(d)] = 1

def deck_in_history(d):
	global played_decks
	if generate_history_key(d) in played_decks.keys():
		return 1
	else:
		return 0	

def score_deck(d):
	tot = 0
	multiplier = 1
	while(d):
		tot += multiplier*d.pop()
		multiplier+=1
	return tot

def play_game(d):
	local_deck = d
	while len(local_deck[0]) > 0 and len(local_deck[1]) > 0:
		c0 = local_deck[0].pop(0)
		c1 = local_deck[1].pop(0)
		if c0 > c1:
			local_deck[0].append(c0)
			local_deck[0].append(c1)
		else:
			local_deck[1].append(c1)
			local_deck[1].append(c0)	
	return local_deck

def play_recursive_game(g):
	global final_deck
	winner = -1
	hand = [g.hand0,g.hand1]
	while len(hand[0]) > 0 and len(hand[1]) > 0:
		if deck_in_history(hand):
			return 0
			break
		else:
			store_deck_history(hand)
			c0 = hand[0].pop(0)
			c1 = hand[1].pop(0)
			if len(hand[0]) >= c0 and len(hand[1]) >= c1:
				new_game = Game(hand[0],hand[1])
				winner = play_recursive_game(new_game)
			else:
				if c0 > c1:
					winner = 0
				else:
					winner = 1
			if winner == 0:
				hand[0].append(c0)
				hand[0].append(c1)
			else:
				hand[1].append(c1)
				hand[1].append(c0)
	
	final_deck = hand 
	return winner

f = open("input22-test.txt","r")
data = f.read().splitlines()
f.close()

deck = [[]]
temp_deck_2 = []
side = 1
for d in data:
	if 'Player 2' in d:
		side = 2
	if d != "" and not "Player" in d:
		if side == 1:
			deck[0].append(int(d))
		else:
			temp_deck_2.append(int(d))
deck.append(temp_deck_2)

print(deck)
p1_deck = deck.copy()		
p2_deck = deck.copy()
		
#dd = play_game(p1_deck)
#if len(dd[0]) > 0:
#	print(score_deck(dd[0]))
#else:
#	print(score_deck(dd[1]))
	
p2_game = Game(deck[0],deck[1])
final_winner = play_recursive_game(p2_game)
print(score_deck(final_deck[final_winner]))
