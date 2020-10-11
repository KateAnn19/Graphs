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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
                    # print("This is the final path ", path)
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
            # print("Neigh after get neighbors in bft", neigh)
            for n in neigh:
                new = list(path)
                new.append(graph[current_node][n])
                queue.append(new)


def dft(myRooms, graph, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # print(f"starting value in DFT {starting_vertex} \n")
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
            # print(f"Neighs in dft before loop {neighs} \n")
################################################################################################################
            # print('THIS IS CURRENT: ', graph[curr])
            # for key,value in graph[curr].items():
            #    print(key, value)
            #    if(value == '?'):
                   #travel?
                   #mark edges?

            if len(neighs) > 1:
                for i in neighs:
                    if neighs[i] == '?':
                        # this adds neighbors to the path which keeps the while loop going
                        # print(f"This is i in the DFT loop {i}")
                        player.travel(i)
                        # print(f"CURR {curr}")
                        # print(f"Current Room {player.current_room.id}")
                        # print(f"This is i Before calling markEdges _> {i}")
                        markEdges(graph, curr, i, player.current_room.id)
                        # print(f"GRAPH AFTER MARK EDGES {graph}")
                        traversal_path.append(i)
                        # print(f"CURRENT ROOM ID {player.current_room.id}")
                        myRooms.add(player.current_room)

                        paths.push(player.current_room.id)
                        break

################################################################################################################
            else:
                for i in neighs:
                    if neighs[i] == '?':
                        # this adds neighbors to the path which keeps the while loop going
                        # print(f"This is i in the DFT loop {i}")
                        player.travel(i)
                        # print(f"CURR {curr}")
                        # print(f"Current Room {player.current_room.id}")
                        # print(f"This is i Before calling markEdges _> {i}")
                        markEdges(graph, curr, i, player.current_room.id)
                        # print(f"GRAPH AFTER MARK EDGES {graph}")
                        traversal_path.append(i)
                        # print(f"CURRENT ROOM ID {player.current_room.id}")
                        myRooms.add(player.current_room)
                        paths.push(player.current_room.id)
                        # break
    # print(f"End of DFT Graph looks like {graph}")

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
    # loop with DFT
    while len(myRooms) < len(room_graph):
        dft(myRooms, unvisitedGraph, player.current_room.id)
        
        # print(f"DEAD END {player.current_room.id} \n")
        returnValues = bfs(unvisitedGraph, player.current_room.id, "?")
        # print(f"Return Values {returnValues} \n")
        # print(f"UNVISITED GRAPH {unvisitedGraph} \n")
        # print("AFTER BFS HAS BEEN CALLED ", player.current_room.id)
        # print("Length of Rooms ", len(myRooms))
        # print(len(room_graph))
        if(len(myRooms) < len(room_graph)):
            shortestPath = returnValues[1]
            len(shortestPath)
            if len(shortestPath) > 0:

            # print("SHORTEST PATH ",shortestPath)
            # print(len(room_graph))
                for p in shortestPath:
                    # print("THIS IS P ", p)
                    traversal_path.append(p)
                    player.travel(p)
        else:
            return 
            
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


