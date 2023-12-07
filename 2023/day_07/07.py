hand_types = {'5K': 7,
              '4K': 6,
              'FH': 5,
              '3K': 4,
              '2P': 3,
              '1P': 2,
              'HC': 1}

card_rank = '23456789TJQKA'

class Hand():
    def __init__(self,s,bet):
        self.cards = s
        self.bet = int(bet)
        self.counts = {'A':0,'K':0,'Q':0,'J':0,'T':0,'9':0,'8':0,'7':0,'6':0,'5':0,'4':0,'3':0,'2':0}
        self.hand_type = self.calc_hand_type()

    def calc_hand_type(self):
        for char in self.cards:
            self.counts[char] += 1
        sorted_cards = sorted(self.counts.items(),key=lambda x:x[1],reverse =True)
        if sorted_cards[0][1] == 5:
            return hand_types['5K']
        elif sorted_cards[0][1] == 4:
            return hand_types['4K']
        elif sorted_cards[0][1] == 3:
            if sorted_cards[1][1] == 2:
                return hand_types['FH']
            else:
                return hand_types['3K']
        elif sorted_cards[0][1] == 2:
            if sorted_cards[1][1] == 2:
                return hand_types['2P']
            else:
                return hand_types['1P']
        else:
            return hand_types['HC']
    
def sort_indices(h):
    return (h.hand_type,
            card_rank.index(h.cards[0]),
            card_rank.index(h.cards[1]),
            card_rank.index(h.cards[2]),
            card_rank.index(h.cards[3]),
            card_rank.index(h.cards[4])
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