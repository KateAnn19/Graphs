#write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consits of 1s that are connected to the north, south, east or west
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)




islands = [     [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1] ]

islands_two = [[0, 1, 0, 1, 0, 0],
               [1, 1, 0, 1, 1, 0],
               [0, 0, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0],
               [1, 1, 0, 0, 0, 0] ]                 

# island_counter(islands) # returns 4 

def get_neighbors(row, col, island_matrix):
   
    neighbors = []
    # check the neighbor above row and col
    if row > 0 and island_matrix[row -1][col] == 1:
        neighbors.append((row - 1, col))
    # check the neighbor below row and col
    if row < len(island_matrix) - 1 and island_matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    # check the neigh left row and col
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    # check the neighbor right row and col
    if col <  len(island_matrix[row]) - 1 and island_matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors

def dft(starting_row, starting_col, island_matrix, visited):
    # create an empty stack
    new_stack = Stack()
    # push the starting row and col onto stack
    new_stack.push((starting_row, starting_col))
    # while stack is not empty:
    while new_stack.size() > 0:
        # pop the current row and col off the stack
        curr_row_col = new_stack.pop()
        row = curr_row_col[0]
        col = curr_row_col[1]
        # if current row and col NOT visited
        if visited[row][col] is False:
            #set the current and col as visited 
            visited[row][col] = True
            #get the neighbor rows and columns
           
            for neighbor in get_neighbors(row, col, island_matrix):
               
                # push them onto the stack 
                new_stack.push(neighbor)
    return visited 

def island_counter(island_matrix):
    # keep track of all visited vertices
    visited_matrix = []
    for i in range(len(island_matrix)):
        visited_matrix.append([False] * len(island_matrix[0]))
    island_count = 0
    # walk through each cell of the matrix
    for row in range(len(island_matrix)):
        for col in range(len(island_matrix[row])):
            if island_matrix[row][col] == 1 and visited_matrix[row][col] is False:
        # if a cell value is 1 and has not been visited, that's the start of an island
            # traverse the connected component (graph)
                visited_matrix = dft(row, col, island_matrix, visited_matrix) #because of pass by reference the visited_matrix gets changed
                island_count += 1
                # (can do DFT or BFT) DFT starting at current cell
        # Once we are done DFT, that means we have found a new Island
        # increment some island_count value + 1

    return island_count 


print(island_counter(islands_two))