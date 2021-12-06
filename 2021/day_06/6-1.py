
def process_day(fish):
  new_fish_count = [0,0,0,0,0,0,0,0,0]
  for i in range(1,9):
    new_fish_count[i-1] = fish[i]
  new_fish_count[6] += fish[0]
  new_fish_count[8] += fish[0]
  return new_fish_count  

fish_count = [0,0,0,0,0,0,0,0,0]

f=open("input6.txt","r")
input_fish = f.readline().strip().split(",")
for fish in input_fish:
  fish_count[int(fish)] += 1

for d in range(256):
  fish_count = process_day(fish_count)

total_fish = sum(fish_count)
print("Total fish is: ",total_fish)
