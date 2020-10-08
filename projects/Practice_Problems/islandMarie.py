from collections import deque
    #HOW TO SOLVE ANY GRAPH PROBLEM:

#Translate the problem into graph terminology
    #What are the vertices, edges, weights (if needed)?

""""
Vertices: islands
Edges: 1's that are connected
Weights: None
"""""

""""
Plan
1. translate the problem into graph terminology
vertex - is a cell
edge - neighboring cells

2. Build your graph 
it's the grid so need to build it!

3. traverse your graph/grid
go through each element in the grid
if we finda 1, increment num islands, then we want to traverse all of its
connected components and mark them as visited 
return numIslands 

"""""


#Build your graph
    #Do you even need to build a graph? Should you use an adjacency matrix/list?

#Traverse your graph
    #Should you use BFS/DFS? Do you need an auxiliary data structure? (list containing path?)

# Start at x, y and mark connected components that are 1 visited    
def markConnectedComponentsAsVisited(grid, visited, x, y):
    width, height = len(grid[0], len(grid))
    stack = deque()
    stack.append((x,y))
    while len(stack) > 0:
        x, y = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        # Traverse all adjacent nodes that are also 1
        # Check left node
        if x - 1 >= 0 and grid[y][x - 1] == '1':
            stack.append((x - 1, y))
            # Check right node
        if x + 1 < width and grid[y][x + 1] == '1':
            stack.append((x + 1, y))
            # Check top node
        if y - 1 >= 0 and grid[y][x - 1] == '1':
            stack.append((x - 1, y))
            # Check bottom node
        if y + 1 < height and grid[y][x - 1] == '1':
            stack.append((x - 1, y))
         
            
    
def numIslands(grid):
    if len(grid) == 0:
        return 0
    width, height = len(grid[0]), len(grid)
    #visited[i][j] is True if cell in grid[i][j] has been visited
    visited = [[False] * width for x in range(height)]
    
    # double for loops
    # traverse through each 
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '1' and not visited[y][x]:
                numIslands += 1
                markConnectedComponentsAsVisited(grid, visited, x, y)
    return numIslands


input1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
] 


input2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "0"]
] 




print(numIslands(input1))


