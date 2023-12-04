def parse_line(l):
    items = l.split(':')
    card_num = int(items[0].split()[1])
    nums = items[1].split('|')
    winners = [int(i) for i in nums[0].split()]
    tries = [int(i) for i in nums[1].split()]
    return card_num, winners, tries 

lines = []
#with open('04-test.txt') as f:
with open('04-input.txt') as f:
    lines = f.read().splitlines()
total_score = 0
card_counts = [0]*205
for l in lines:
    num_of_winners = 0
    card_num, winners, tries = parse_line(l)
    card_counts[card_num] += 1
    for t in tries:
        if t in winners:
            num_of_winners += 1
    if num_of_winners > 0:
        total_score += 2**(num_of_winners-1)
        for n in range(num_of_winners):
            card_counts[card_num + n + 1] += card_counts[card_num]

print("part 1: ", total_score)
print("part 2: ", sum(card_counts))