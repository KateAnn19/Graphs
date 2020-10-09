from collections import deque

"""""
#HOW TO SOLVE ANY GRAPH PROBLEM:

#Translate the problem into graph terminology
    #What are the vertices, edges, weights (if needed)?

Vertex: Cities
Edges: paths from one city to another (relationships between veryices)
Weights: None

#Build your graph
    #Do you even need to build a graph? Should you use an adjacency matrix/list?
    {
        London: {New York},
        New York: {Lima},
        Lima: {Sao Paulo}
    }

#Traverse your graph
    #Should you use BFS/DFS? Do you need an auxiliary data structure? (list containing path?)
    We can traverse the graph in any way, if we find that the node we're currently on doesn't have any outgoing edges,
    then we've found the destination city 
"""""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 0:
            return ''
        # calls the function that creates the graph out of the list 
        graph = self.createGraph(paths)
        stack = deque()
        stack.append(paths[0][0])
        visited = set()
        while len(stack) > 0:
            curr = stack.pop()
            #don't want to visit it again
            visited.add(curr)
            if curr not in graph: # curr is not a key
                return curr
            else:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return ''

    # this builds the graph (adjacency list)
    # returns a dictionary source --> {destination}
    """
    [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

    graph = {
        "London": {New York},
        "New York": {Lima},
        "Lima": {Sao Paulo}  # Sao Paulo is not a key in this graph (it IS the destination city)
    }
    """
    def createGraph(self, paths):
        graph = {}
        for edge in paths:
            origin, destination = edge[0], edge[1]
            if origin in graph:
                graph[origin].add(destination)
            else: graph[origin] = {destination}
        return graph



paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# Output: "Sao Paulo"
