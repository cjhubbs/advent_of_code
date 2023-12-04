lines = []
#with open('04-test.txt') as f:
with open('04-input.txt') as f:
    lines = f.read().splitlines()
total_score = 0
cur_card = 1
card_counts = [0]*205
for l in lines:
    card_counts[cur_card] += 1
    winners = {}
    tokens = l.split()
#    for i in range(2,7):
    for i in range(2,12):
        winners[tokens[i]] = 0
#    for i in range(8,16):
    for i in range(13,38):
        if tokens[i] in winners.keys():
            winners[tokens[i]] += 1
    num_of_winners = 0
    for v in winners.values():
        if v > 0:
            num_of_winners += 1
    if num_of_winners > 0:
        total_score += 2**(num_of_winners-1)
        for n in range(num_of_winners):
            card_counts[cur_card + n + 1] += card_counts[cur_card]
    cur_card += 1

print("part 1: ", total_score)
print("part 2: ", sum(card_counts))