# import sys
# sys.path.append('./util')
from util import Queue, Stack  # These may come in handy
import collections

"""
Simple graph implementation
"""



class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = { # space O(v) + O(e)
            # 1: {2},
            # 2: {3, 4},
            # 3: {5},
            # 4: {6,7},
            # 5: {3},
            # 6: {3},
            # 7: {1,6}
        }
    # to get edges that are pointed back to the node 
    # def add_bidirected_edge(self, v1, v2):
    #     self.add_edge(v1, v2)
    #     self.add_edge(v2, v1)
        self.visited_set = set()
        self.path = []

    def add_vertex(self, vertex_id): #time complexity is O(1)
        """                                   
        Add a vertex to the graph.
        """
        # create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):    #time complexity is O(1)
        """
        Add a directed edge to the graph.
        """
        #find vertex V1 in our vertices, add V2 to the set of edges 
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):   #time complexity is O(1)
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        current_vertex_queue = Queue()
        current_vertex_queue.enqueue(starting_vertex)
        # create an empty set to track visited vertices 
        visited = set()
        # while the queue is not empty:
        while current_vertex_queue.size() > 0:
            # get current vertex (dequeque from queue)
            curr = current_vertex_queue.dequeue()
            #Check if the current vertex has not been visited:
            if curr not in visited:
                # print the current vertex
                print(curr)
                # mark the current vertex as visited
                    # add the current vertex to a visited_set 
                visited.add(curr)
                # queue up all the current vertice's neighbors (so we can visit them next)
                neigh = self.get_neighbors(curr)
                for i in neigh:
                    current_vertex_queue.enqueue(i)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #Create an empty stack and add the starting_vertex
        paths = Stack()
        paths.push(starting_vertex)
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
                neighs = self.get_neighbors(curr)
                for i in neighs:
                    # this adds neighbors to the path which keeps the while loop going
                    paths.push(i)

    # def visited(self, vertex):
    #     visited_set = set()
    #     visited_set.add(vertex)
    #     def dft_recursive(vertex):
    #         nonlocal visited_set
    #         print(vertex)
    #         neighs = self.get_neighbors(vertex)
    #         for i in neighs:
    #             if i not in visited_set: 
    #                 self.visited(i)
    #                 print("this is i", i)
    #                 self.dft_recursive(i)
    #     print("reached here")
    #     dft_recursive(vertex)
    #     return visited_set

    
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        neighs = self.get_neighbors(starting_vertex)
        print(starting_vertex)
        self.visited_set.add(starting_vertex)
        for i in neighs:
            if i not in self.visited_set: 
                self.visited_set.add(i)
                self.dft_recursive(i)
                           

    #
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        queue = []
        # add the starting vertex to the queue initialized as a list
        queue.append([starting_vertex])
        # create a set to store visited values in it to avoide infinite loops
        visited = set()
        # while vertices haven't been visited, loop (while the queue isn't empty)
        while len(queue) > 0:
            # pop off the first element in the list
            path = queue.pop(0)
            # grab the last element in the path 
            current_node = path[-1]
            # if the node isn't in visited, add it
            if current_node not in visited:
                visited.add(current_node)
                # if the node is the destination then return the path
                if current_node == destination_vertex:
                    return path
            # it is not the destination so grab that node's neighbors 
            neigh = self.get_neighbors(current_node)
            # loop through the node's neighbors since these are a set 
            for n in neigh:
                new = list(path)
                new.append(n)
                queue.append(new)

    def bfs_v(self, start, dest):
        queue = Queue()
        visited = set()
        queue.enqueue({
            'current_vertex': start,
            'path': [start]
        })
        queue.enqueue([start])
        while queue.size() > 0:
            curr_obj = queue.dequeque()
            curr_path = curr_obj['path']
            curr_vert = curr_obj['curr_vertex']

            if curr_vert not in visited:

                if curr_vert == dest:
                    return curr_path
                visited.add(curr_vert)

                for v in self.get_neighbors(curr_vert):
                    new_path = list(curr_path)
                    new_path.append(v)
                    queue.enqueue({
                        'current_vert': v,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        current_vertex_stack = Stack()
        current_vertex_stack.push([starting_vertex])
        # create an empty set to track visited vertices
        visited = set() 
        # while the queue is not empty:
        while current_vertex_stack.size() > 0: 
            # get current vertex PATH (dequeque from queue)
            curr_path = current_vertex_stack.pop()
            # set the current vertex to the LAST element of the PATH
            current_vertex = curr_path[-1]
            #Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if current_vertex == destination_vertex:
                    # IF IT IS, STOP AND RETURN  
                    return curr_path  
                # mark the current vertex as visited
                    # add the current vertex to a visited_set 
                visited.add(current_vertex)
                # queue up NEW paths with each neighbor:
                    # take current path
                neigh = self.get_neighbors(current_vertex)          
                    # append the neighbor to it
                for i in neigh: 
                    new_path = list(curr_path)
                    new_path.append(i)
                    # queue up NEW path
                    current_vertex_stack.push(new_path)
       

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            path1 = []
            for i in self.path:
                path1.append(i[0])
            path1.append(starting_vertex)
            return path1
        self.path.append([starting_vertex])
        neighs = self.get_neighbors(starting_vertex)
        new_path = []
        new_path.append(starting_vertex)
        for i in neighs:
            if i not in self.visited_set: 
                new_path.append(i)
                self.visited_set.add(i)
        return self.dfs_recursive(i, destination_vertex)
                    

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    #print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)
    # print(" ")
    # print(graph.dft(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(4, 2))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
