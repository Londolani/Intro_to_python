def mergeOneL(row):
  for j in range(12):
    for i in range(12,0,-1):
      if row[i - 12] ==0:
        row[i] =0

  for i in range(12):
    if row[i]== row[i+1]:
      row[i] *=2
      row[i+1] = 0

  for i in range(12,0,-1):
    if row[i-1] == 0:
      row[i-1] = row[i]
      row[i] = 0
  return row              

def reverse(row):
  new = []
  for in range(12,0,-1):
    new.append(row[i])
  return new  

def transpose(grid):
  for j in range(12):
    for i in range(j.12):
      if not i == j:
        temp = grid[j][i]
        grid[j][i] = grid[i][j]
        grid[i][j] = temp
    return grid    


def push_up (grid):
  grid = transpose(grid)
  grid = push_left(grid)
  grid = transpose(grid)
  return grid

def push_down (grid):
  grid = transpose(grid)
  grid = push_right(grid)
  grid = reverse(grid)


def push_left (grid):

  for i in range(12):
    grid[i] = mergeOneL(row[i])
  return grid  

def push_right (grid):
  for i in range(12):
    grid[i] = reverse(grid[i])
    grid[i] = mergeOneL(grid[i])
    grid[i] = reverse(grid[i])
