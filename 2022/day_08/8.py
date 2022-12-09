import numpy as np

class Forest():
  def __init__(self,grid):
    self.dim = len(grid)
    self.g = np.array(grid).astype(np.int32)
    self.v = np.zeros((self.dim, self.dim),dtype=np.int32)
    self.score = np.zeros((self.dim, self.dim),dtype=np.int32)

  def process_row(self, row, reverse=False):
    if reverse:
      max = self.g[row][-1]
      for i in reversed(range(self.dim)):
        if self.g[row][i] > max:
          self.v[row][i] = 1
          max = self.g[row][i]      
    else:
      max = self.g[row][0]
      for i in range(self.dim):
        if self.g[row][i] > max:
          self.v[row][i] = 1
          max = self.g[row][i]

  def process_col(self, col, reverse=False):
    
    if reverse:
      max = self.g[-1][col]
      for i in reversed(range(self.dim)):
        if self.g[i][col] > max:
          self.v[i][col] = 1
          max = self.g[i][col]      
    else:
      max = self.g[0][col]
      for i in range(self.dim):
        if self.g[i][col] > max:
          self.v[i][col] = 1
          max = self.g[i][col]      
                    
  def set_edges_visible(self):
    self.v[0,:] = 1
    self.v[-1,:] = 1
    self.v[:,0] = 1
    self.v[:,-1] = 1
    
  def total_visible(self):
    return np.count_nonzero(self.v)
    
  def east(self, row, col):
    full_vect = self.g[row,:]
    vect = full_vect[col+1:]
    return vect
  
  def west(self, row, col):
    full_vect = self.g[row,:]
    vect = full_vect[:col][::-1]
    return vect
  
  def north(self, row, col):
    full_vect = self.g[:,col]
    vect = full_vect[:row][::-1]
    return vect 
  
  def south(self, row, col):
    full_vect = self.g[:,col]
    vect = full_vect[row+1:]
    return vect
    
  def vec_visibility(self, h, vect):
    if len(vect) > 0:
      count = 0
      for v in vect:
        count += 1
        if v >= h:
          return count
      return count
    else:
      return 0
        
  def vis_score(self, r, c):
    t = self.g[r][c]
    east_vec = self.east(r,c) 
    east_vis = self.vec_visibility(t, east_vec)
    
    west_vec = self.west(r,c)
    west_vis = self.vec_visibility(t,west_vec)
    
    north_vec = self.north(r,c)
    north_vis = self.vec_visibility(t,north_vec)
    
    south_vec = self.south(r,c)
    south_vis = self.vec_visibility(t,south_vec)
        
    return north_vis * south_vis * east_vis * west_vis
    
  def max_vis(self):
    vec = self.score.reshape(-1)
    return(vec.max())
          
  def calculate_visibility_scores(self):
    for r in range(self.dim):
      for c in range(self.dim):
        self.score[r][c] = self.vis_score(r,c)

if __name__ == "__main__":
  
  with open('8-input.txt') as f:
    lines = f.read().splitlines()
  f.close()
  
  grid = []
  for l in lines:
    grid.append([*l])
  
  f = Forest(grid)
  f.set_edges_visible()
  
  for r in range(len(lines)):
    f.process_row(r)
    f.process_row(r,True)  
    f.process_col(r)
    f.process_col(r,True)
  
  print("P1:", f.total_visible())
  
  f.calculate_visibility_scores()
  print("P2:" ,f.max_vis())
