
def count_islands(grid):
    '''Takes a 2D grid (list of lists) of 0s (water) and 1s (land)
      and returns the number of islands present
      (an island is defined by and connected to land horizontally or
      vertically)
      
      assume all rows in the grid are the same length
      assume all positions in the grid will contain a 0 or a 1
      
      '''
      
    islands = 0
    land = []
    
    # check edge case of empty grid
    if not grid:
        return islands
        
    # check dimensions of the grid 
    height = len(grid)
    width = len(grid[0])
    # loop through the positions on the grid
    for row in range(0, height):
        for column in range(0, width): 
            # if land, determine if connected to other land
            if grid[row][column] == 1:
                options = add_surroundings(grid, row, column)
                land = False
                while options:
                    current = options.pop(-1)
                    if current == 1:
                      land = True
                      break
                # if connected to land, need to determine if new island or part of existing
                if land:
                
    
def add_surroundings(grid,row, column)
    height = len(grid)
    width = len(grid[0])
    surroundings = []
    if (column > 0):
        surroundings.append(grid[row][column-1])
    if (column < width):
        surroundings.append(grid[row][column+1])
    if (row > 0):
        surroundings.append(grid[row-1][column])
    if (row < height):
        surroundings.append(grid[row+1][column])
      
    return surroundings
          
print()
print(count_islands([[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0],[0,0,0,0,0]]) == 1)

# 1 1 1 1 0
# 1 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0


print()
print(count_islands([[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]) == 3)

# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 1

print()
print(count_islands([[0,0,0,0,0], [0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0]]) == 0)

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

print()
print(count_islands([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1],[1,1,1,1,1]]) == 1)
    
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
    