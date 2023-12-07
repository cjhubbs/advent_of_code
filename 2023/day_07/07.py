hand_types = {'5K': 7,
              '4K': 6,
              'FH': 5,
              '3K': 4,
              '2P': 3,
              '1P': 2,
              'HC': 1}

p1_card_rank = '23456789TJQKA'
p2_card_rank = 'J23456789TQKA'
jokers_active = False

def sort_card_counts(c):
    if jokers_active:
        return (c[1],p2_card_rank.index(c[0]))
    else:
        return (c[1],p1_card_rank.index(c[0]))

class Hand():
    def __init__(self,s,bet):
        self.cards = s
        self.bet = int(bet)
        self.counts = {'A':0,'K':0,'Q':0,'J':0,'T':0,'9':0,'8':0,'7':0,'6':0,'5':0,'4':0,'3':0,'2':0}
        self.hand_type = self.calc_hand_type(False)
        self.joker_hand_type = self.calc_hand_type(True)

    def calc_hand_type(self,jokers_wild):
        jokers = 0
        for c in self.counts.keys():
            self.counts[c] = 0
        for char in self.cards:
            self.counts[char] += 1
        if jokers_wild:
            jokers = self.counts['J']
            self.counts['J'] = 0
            if jokers == 5:
                return hand_types['5K']

        sorted_cards = sorted(self.counts.items(),key=sort_card_counts,reverse =True)
        max_sorted = sorted_cards[0][1]
        if jokers_wild:
            max_sorted += jokers
        if max_sorted == 5:
            return hand_types['5K']
        elif max_sorted == 4:
            return hand_types['4K']
        elif max_sorted == 3:
            if sorted_cards[1][1] == 2:
                return hand_types['FH']
            else:
                return hand_types['3K']
        elif max_sorted == 2:
            if sorted_cards[1][1] == 2:
                return hand_types['2P']
            else:
                return hand_types['1P']
        else:
            return hand_types['HC']
    
def sort_indices(h):
    return (h.hand_type,
            p1_card_rank.index(h.cards[0]),
            p1_card_rank.index(h.cards[1]),
            p1_card_rank.index(h.cards[2]),
            p1_card_rank.index(h.cards[3]),
            p1_card_rank.index(h.cards[4])
            )

def joker_sort_indices(h):
    return (h.joker_hand_type,
            p2_card_rank.index(h.cards[0]),
            p2_card_rank.index(h.cards[1]),
            p2_card_rank.index(h.cards[2]),
            p2_card_rank.index(h.cards[3]),
            p2_card_rank.index(h.cards[4])
            )

if __name__ == "__main__":
    
    hands = []
    with open('07-input.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        parts = l.split()
        hands.append(Hand(parts[0],parts[1]))
    sorted_hands = sorted(hands,key=sort_indices)
    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += (i+1)*sorted_hands[i].bet
    print("p1 winnings: ",winnings)

    jokers_active = True
    sorted_hands = sorted(hands,key=joker_sort_indices)
    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += (i+1)*sorted_hands[i].bet
    print("p2 winnings: ",winnings)