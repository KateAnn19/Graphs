from util import Queue, Stack  # These may come in handy
import collections


#HOW TO SOLVE ANY GRAPH PROBLEM:

#Translate the problem into graph terminology
    #What are the vertices, edges, weights (if needed)?

# Vertex:
# Edge: 
# Weights: None

# Path from one vertex to another 
    # Path - transformation 

#Build your graph
    #Do you even need to build a graph? Should you use an adjacency matrix/list?
    # we can create all possible transformations of beginWord 
    # and all possible transformations of its transformations
    # BUT that would waste A LOT OF MEMORY

    #INSTEAD, what we can do is find out the next vertex (word) by coming up with all valid one character transformations
    # and seeing if those are valid vetices to visit (it it's in the word list)
    
    
    
# if tied return lowest value
# if not found return -1

# vertices - ancestors
# edges connections between ancestors
# neighbors 
# keep a PATH list

def get_neighbors(ancestors, current_vertex):
    for i in ancestors:
        print(i)
        if i[1] == current_vertex:
            return i[0]
    #return current_vertex

        


def earliest_ancestor(ancestors, starting_node):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    paths = Stack()
    paths.push(starting_node)
    # Create an empty set to track visited vertices
    visited = set()
    # while the stack is not empty:
    while paths.size() > 0:
        # get current vertex (pop from stack)
        curr = paths.pop()
        # Check if the current vertex has not been visited:
        if curr not in visited: 
            #print the current vertex
            print(curr)
            #mark the current vertex as visited
            visited.add(curr)
                # Add the current vertex toa  visited_set
            # push up all the current vertex's neighbors (so we can visit them next)
            print("curr",curr)
            neighs = get_neighbors(ancestors, curr)
            print("neighs",neighs)
            
            if(neighs == None):
                if curr == starting_node:
                    return -1
                return curr
           
            
            #for i in neighs:
                # this adds neighbors to the path which keeps the while loop going
            paths.push(neighs)
    
    # current_vertex_stack = Stack()
    # current_vertex_stack.push([starting_node])
    # # create an empty set to track visited vertices
    # visited = set() 
    # # while the queue is not empty:
    # while current_vertex_stack.size() > 0: 
    #     # get current vertex PATH (dequeque from queue)
    #     curr_path = current_vertex_stack.pop()
    #     # set the current vertex to the LAST element of the PATH
    #     current_vertex = curr_path[-1]
    #     #Check if the current vertex has not been visited:
    #     if current_vertex not in visited:
    #         # mark the current vertex as visited
    #             # add the current vertex to a visited_set 
    #         visited.add(current_vertex)
    #         # queue up NEW paths with each neighbor:
    #             # take current path
    #         neigh = get_neighbors(ancestors, current_vertex)          
    #             # append the neighbor to it
    #         #for i in neigh: 
    #         new_path = list(curr_path)
    #         new_path.append(neigh)
    #             # queue up NEW path
    #         current_vertex_stack.push(new_path)
    # return curr_path






        