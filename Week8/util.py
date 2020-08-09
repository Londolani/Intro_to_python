import numpy as np

def create_grid(grid):
  grid = np.zeros((4, 4))

def print_grid (grid):
  grid = np.zeros((20, 20))

def check_lost (grid):
  flag = False
  for row in grid:
    for c in row:
      if c != 0 and c:
        flag = True
        break

def check_won (grid):
  flag = False
  for row in grid:
    for c in row:
      if c >= 32 :
        flag = True
        break

def copy_grid (grid):
  return grid

def grid_equal(grid1,grid2):
  for i in range(grid1):
    for j in range(grid2):
      if grid1[i] == grid2[j]
  return true