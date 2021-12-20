import numpy 
import time 

def b2d(v):
  factor = 1
  ret = 0
  for i in reversed(range(9)):
    ret += v[i]*factor
    factor *= 2 
  return ret 

start = time.time()
# array will expand outward by 1 in each direction each cycle, so size it accordingly
num_of_cycles = 50
buffer_left = num_of_cycles

f = open("input20.txt","r")
pixel_index = f.readline().strip()
lines = f.readlines()
input_len = len(lines[0])-1

buffer = num_of_cycles+1
arr_dim = input_len + ((buffer)*2)
image = numpy.zeros((arr_dim,arr_dim) ,dtype=int)

j = 0
for l in lines:
  l = l.strip()
  for i in range(len(l)):
    if l[i] == "#":
      image[j+buffer][i+buffer] = 1
  j += 1

# the fill digit for extending the buffer area
edge_digit = 1

for c in range(num_of_cycles):

  new_image = numpy.zeros((arr_dim,arr_dim),dtype=int)
  for row in range(arr_dim-2):
    for col in range(arr_dim-2):
      slice = image[row:row+3, col:col+3]
      slice = numpy.reshape(slice,9)
      new_pixel = pixel_index[b2d(slice)]
      if new_pixel == "#":
        new_image[row+1][col+1] = 1
  
  # fill in the edges to simulate the 'infinite' nature of the image
  # digit swaps since pixel encoder is set to swap background every cycle
  for i in range(buffer_left):
    new_image[i,:] = edge_digit
    new_image[:,i] = edge_digit
    new_image[:,arr_dim-1-i] = edge_digit
    new_image[arr_dim-1-i,:] = edge_digit
  buffer_left -= 1
  image = numpy.copy(new_image)

  edge_digit = 1 if edge_digit == 0 else 0

pixel_count = numpy.count_nonzero(image)
print("final pixel count is",pixel_count)
end = time.time()
print("t = ",end-start)
