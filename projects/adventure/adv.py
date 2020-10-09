from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from collections import deque


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


# Load world
world = World()

# map_file = "maps/test_line.txt"
# shortest is 2
# map_file = "maps/test_cross.txt"
# shortest is 14
# map_file = "maps/test_loop.txt"
# shortest is 14
# map_file = "maps/test_loop_fork.txt"
# shortest is 24
# map_file = "maps/main_maze.txt"
# shortest is 918

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()  # (0,4) X,Y coords of graph

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
################################################################################################################################################


def get_neighbors(graph, vertex_id):  # time complexity is O(1)
    """
    Get all neighbors (edges) of a vertex.
    """
    if graph[vertex_id]:
        return graph[vertex_id]


def bfs(graph, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # create an empty queue and enqueue the PATH TO starting_vertex
    queue = []
    directionQ = []
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
            for i in graph[current_node]:
                if graph[current_node][i] == destination_vertex:
                    # player.travel(i)
                    #markEdges(graph, current_node, i, player.current_room.id)
                    print("This is the final path ", path)
                    for ele in range(len(path)):
                        # print("this is ele ", ele)
                        # print(graph[path[ele]])
                        for dir in graph[path[ele]]:
                            if (ele + 1) > len(path) - 1:
                                return path, directionQ
                            elif graph[path[ele]].get(dir) == path[ele + 1]:
                                directionQ.append(dir)
            # it is not the destination so grab that node's neighbors
            neigh = get_neighbors(graph, current_node)
            # loop through the node's neighbors since these are a set
            print("Neigh after get neighbors in bft", neigh)
            for n in neigh:
                new = list(path)
                new.append(graph[current_node][n])
                queue.append(new)


def dft(myRooms, graph, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    print("starting", starting_vertex)
    # Create an empty stack and add the starting_vertex
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
            # mark the current vertex as visited
            visited.add(curr)
            # Add the current vertex toa  visited_set
            # push up all the current vertex's neighbors (so we can visit them next)
            neighs = get_neighbors(graph, curr)
            print("Neighs in dft before loop", neighs)
            for i in neighs:
                if neighs[i] == '?':
                    # this adds neighbors to the path which keeps the while loop going
                    print("This is i in the loop ",i)
                    player.travel(i)
                    myRooms.add(player.current_room)
                    markEdges(graph, curr, i, player.current_room.id)
                    traversal_path.append(i)
                    paths.push(player.current_room.id)


def markEdges(unvisitedGraph, prev_room=None, prev_room_choice=None, id=None):
    unvisitedGraph[prev_room][prev_room_choice] = id
    if prev_room_choice == "n":
        bidirectional = "s"
    elif prev_room_choice == "s":
        bidirectional = "n"
    elif prev_room_choice == "w":
        bidirectional = "e"
    elif prev_room_choice == "e":
        bidirectional = "w"
    unvisitedGraph[id][bidirectional] = prev_room



def traverseMaze(map):
    unvisitedGraph = createGraph(map)
    current_room_id = player.current_room.id
    # grabs the current room exits
    current_room_exits = player.current_room.get_exits()
    random_choice = random.choice(current_room_exits)
    prev_room = current_room_id
    prev_room_choice = random_choice

    myRooms = set()
    player.current_room = world.starting_room
    myRooms.add(player.current_room)
    player.travel(random_choice)
    markEdges(unvisitedGraph, prev_room,prev_room_choice, player.current_room.id)
    traversal_path.append(prev_room_choice)
    myRooms.add(player.current_room)
    print("BEFORE WHILE ", myRooms)
    # loop with DFT
    while len(myRooms) < len(room_graph):
        # print("INSIDE DFT", player.current_room.id, player.current_room.get_exits())
        dft(myRooms, unvisitedGraph, player.current_room.id)
        
        print(f"DEAD END {player.current_room.id}")
        returnValues = bfs(unvisitedGraph, player.current_room.id, "?")
        print("Return Values ", returnValues)
        print("UNVISITED GRAPH" , unvisitedGraph)
        print("AFTER BFS HAS BEEN CALLED ", player.current_room.id)
        print("Length of Rooms ", len(myRooms))
        shortestPath = returnValues[1]
        print("SHORTEST PATH ",shortestPath)
        for p in shortestPath:
            print("THIS IS P ", p)
            traversal_path.append(p)
            player.travel(p)
            
        # this room is the room with a ? in it, we took the shortest path to get here


def createGraph(paths):
    graph = {}
    for room in range(len(paths)):
        room_paths = paths[room][1]
        room_dict = {}
        for directions in room_paths:
            room_dict[directions] = "?"
        graph[room] = room_dict
    return graph


print(traverseMaze(room_graph))
################################################################################################################################################
# print(f"Current room:::: {player.current_room}")
#print(f"Current room id: {player.current_room.id}")
# print(f"Current room exits {player.current_room.get_exits()}")
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print("VISITED ROOMS", player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# HOW TO SOLVE ANY GRAPH PROBLEM:
# Translate the problem into graph terminology
# What are the vertices, edges, weights (if needed)?
""""
To solve this path, you'll want to construct your own traversal graph. 
You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

Try moving south and you will find yourself in room `5`
which contains exits `['n', 's', 'e']`. 
You can now fill in some entries in your graph:

```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```
"""""
# Vertex: rooms
# Edge: exits depending on what direction
# Weights: none

# Path from one vertex to another
# Path - bft in rooms
""""
There are a few smaller graphs in the 
file which you can test your traversal
method on before committing to the large 
graph. You may find these easier to debug.

Start by writing an algorithm that picks a 
random unexplored direction from the player's current room, 
travels and logs that direction, then loops. 
This should cause your player to walk a depth-first traversal. 
When you reach a dead-end (i.e. a room with 
no unexplored paths), walk back to the nearest 
room that does contain an unexplored path.


You can find the path to the shortest 
unexplored room by using a breadth-first
search for a room with a `'?'` for an exit. 
If you use the `bfs` code from the homework, 
you will need to make a few modifications.


1. Instead of searching for a target vertex, 
you are searching for an exit with a `'?'` 
as the value. If an exit has been explored, 
you can put it in your BFS queue like normal.


2. BFS will return the path as a list of 
room IDs. You will need to convert this 
to a list of n/s/e/w directions before you 
can add it to your traversal path.


If all paths have been explored, you're done!

"""""
# Build your graph
# Do you even need to build a graph?
# Should you use an adjacency matrix/list?
