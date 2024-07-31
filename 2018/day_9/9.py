from collections import deque

def play_game(num_players, last_marble):
    circle = deque([0])
    scores = [0] * num_players
    cur_player = 1
    for i in range(1,last_marble+1):
        if i % 23 == 0:
            circle.rotate(7)
            scores[cur_player] += i + circle.pop() 
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
        cur_player += 1
        if cur_player == num_players:
            cur_player = 0
    return max(scores)

if __name__ == "__main__":
    players = 462
    marbles = 71938
    #p1
    high_score = play_game(players,marbles)
    print(high_score)
    #p2
    marbles = marbles * 100
    high_score = play_game(players,marbles)
    print(high_score)    