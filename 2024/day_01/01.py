
from collections import Counter

def calculate_distance(left,right):
    left.sort()
    right.sort()
    total_diff = 0
    for i in range(len(left)):
        total_diff += abs (left[i] - right[i])
    print(total_diff)

def calculate_similarity(left,right):
    right_counts = Counter(right)
    total = 0
    for l in left:
        if l in right_counts.keys():
            total += (l*right_counts[l])
    print(total)

if __name__ == "__main__":

    filename = "01-input.txt"

    left  = []
    right = []

    with open(filename) as f:
        lines = f.read().splitlines()
    for l in lines:
        temp = l.split()
        left.append(int(temp[0]))
        right.append(int(temp[1]))
    calculate_distance(left,right)
    calculate_similarity(left,right)