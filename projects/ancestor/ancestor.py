from collections import deque
from collections import defaultdict
# HOW TO SOLVE ANY GRAPH PROBLEM:

# Translate the problem into graph terminology
# What are the vertices, edges, weights (if needed)?

# Vertex: person
# Edge: connection to ancestor (parent to child, child to parent)
# Weights: None

# Path from one vertex to another
# Path - dft (farthest ancestor)

# Build your graph
# Do you even need to build a graph?
# Should you use an adjacency matrix/list?

"""""
graph = {
    1: {3},
    2: {3},
    3: {6},
    5: {6, 7},
    4: {5, 8},
    8: {9},
    11: {8},
    10: {1}
}
"""""

# if tied return lowest value
# if not found return -1


def earliest_ancestor(ancestors, starting_node):
    
    graph = createGraph(ancestors)
    stack = deque()
    stack.append((starting_node, 0)) # node, distance from starting_node
    visited = set()
    earliestAncestor = (starting_node, 0)

    while len(stack) > 0:
        curr = stack.pop() # (curr node, distance from starting node)
        currNode, distance = curr[0], curr[1]
        visited.add(curr)
        
        if currNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


# create a graph from input ancestors
def createGraph(edges):
    # every key I add to this dictionary, will have 
    # a default value of set()
    # graph = defaultdict(set)

    graph = {}
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        #graph[child].add(ancestor) ---> defaultdict(set)
        if ancestor in graph:
            graph[ancestor].add(child)
        else:
            graph[acnestor] = {child}
    
    return graph

# def add_bidirected_edge(self, v1, v2):
#     self.add_edge(v1, v2)
#     self.add_edge(v2, v1)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 5))
