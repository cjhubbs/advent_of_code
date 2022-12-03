priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(lines):

  total = 0
  for l in lines:
    half = int(len(l)/2)
    bag_1 = l[:half]
    bag_2 = l[half:]
    for c in bag_1:
      if c in bag_2:
        total += priorities.index(c)
        break
  
  print("P1 total priority is: ", total)
  
def part2(lines):
  total = 0
  for i in range(0,len(lines),3):
    for c in lines[i]:
      if c in lines[i+1] and c in lines[i+2]:
        total += priorities.index(c)
        break
  print("P2 total priority is: ", total)
  
if __name__ == "__main__":
  with open('3-input.txt') as f:
    lines = f.read().splitlines()
  part1(lines)
  part2(lines)
