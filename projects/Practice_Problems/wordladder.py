""""
Sample:
beginWord = "hit",
endWord = "cog,
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
["hit", "hot", "dot", "dog", "cog"]

only change one letter at a time

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
returns an empty list [] because "cog" is not in word list (so no valid transformation)
"""""

#HOW TO SOLVE ANY GRAPH PROBLEM:

#Translate the problem into graph terminology
    #What are the vertices, edges, weights (if needed)?

# Vertex: a word
# Edge: a possible one letter transformation from source vertex to another vertex
        # hot --d--> dot
        # dot --g--> dog
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
"""""

path to word
stack = [hit, hot]
# hit
# *it
# h*t   ----if we get 'hot'  ,   'hot' is in the word list so it's a valid vertex to visit 
# hi*

stack = [[hit, hot, dot, dog, cog], [hit, hot, lot]]
hot
*ot
h*t
ho*

"""""

#Traverse your graph
    #Should you use BFS/DFS? Do you need an auxiliary data structure? (list containing path?)

from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    # breadth first search because we want to find shortest path 
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft() # an array of the current transformations 
        currWord = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        # Determine which vertices to traverse next
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                # Determine if word is in word list (it it's a valid vertex to visit)
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
        # no valid transformation, so an empty array is returned 
        return []      
""""
stack = [hit, hot]
# hit
# *it
# h*t   ----if we get 'hot'  ,   'hot' is in the word list so it's a valid vertex to visit 
# hi*
"""""   
        

