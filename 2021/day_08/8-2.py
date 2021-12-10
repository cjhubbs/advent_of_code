f = open("input8.txt", "r")
data = f.readlines()
parts = [x.strip().split("|") for x in data]

digit_0 = [1, 1, 1, 0, 1, 1, 1]
digit_1 = [0, 0, 2, 0, 0, 1, 0]
digit_2 = [1, 0, 1, 1, 1, 0, 1]
digit_3 = [1, 0, 1, 1, 0, 1, 1]
digit_4 = [0, 1, 1, 1, 0, 1, 0]
digit_5 = [1, 1, 0, 1, 0, 1, 1]
digit_6 = 

inputs = []
outputs = []
for x in parts:
  inputs.append(x[0].split())
  outputs.append(x[1].split())


