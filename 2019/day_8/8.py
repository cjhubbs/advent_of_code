lines = open("8-input.txt", "r").readlines()

width=25
height = 6
ppl = width*height 

#p1
layers = [lines[0][i:i+ppl] for i in range(0,len(lines[0]),ppl)]
min_zeros = ppl
min_zeros_index = 0
for index, l in enumerate(layers):
    zeros = l.count('0')
    if zeros < min_zeros:
        min_zeros = zeros
        min_zeros_index = index
print("p1: ", layers[min_zeros_index].count('1')*layers[min_zeros_index].count('2'))

#p2
output = ""
for c in range(ppl):
    for l in range(len(layers)):
        if layers[l][c] in ['0','1']:
            if layers[l][c] == '0':
                output += '\u2588' #solid block char
            else:
                output += ' '
            break
for h in range(height):
    print(output[h*width:(h*width)+width])