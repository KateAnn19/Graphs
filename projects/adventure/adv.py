from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms() # (0,4) X,Y coords of graph

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

################################################################################################################################################
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


def traverseMaze(map):
    unvisitedGraph = createGraph(map)
    #current room
    print(f"curr_room", player.current_room.id)
    current_room_id = player.current_room.id
    #grabs the current room exits
    current_room_exits = player.current_room.get_exits() 
    #check to see if room are unexplored or not
        #unexplored means the list has a ? 
    #pulls a random direction from list of directions 
    random_choice = random.choice(current_room_exits)
    prev_room = current_room_id
    prev_room_choice = random_choice
    
   
    player.travel(random_choice)
    for i in unvisitedGraph[prev_room]:
        if i == prev_room_choice:
            unvisitedGraph[prev_room][i] = player.current_room.id 
            traversal_path.append(i)
    print(unvisitedGraph)
    #picks a random direction from current room exits and travels there
        #go a certain diretcion but pick from list of exits

def markVisited():
    pass

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

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# print(f"Current room: {player.current_room}")
# print(f"Current room id: {player.current_room.id}")
# print(f"Current room exits {player.current_room.get_exits()}")


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
To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

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
