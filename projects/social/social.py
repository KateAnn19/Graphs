import random
from util import Queue, Stack
from math import *

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        #maps IDs to User Objects
        self.users = {} # {1: User("1"), User("2"), ...}
        #Adjaceny List
        #Maps user_ids to a list of other users (who are their friends)
        self.friendships = {} # {1: {2,3,4}, 2: {1}, 3: {1}, 4: {1} }

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) # {1 : User("mari")}
        #adds vertex to adjacency list
        self.friendships[self.last_id] = set() # {1: ()}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create friendships
        # Generate All possible friendships and put into array
        # 3 users (0, 1, 2)
        # [(0, 1), (0,2), (1,2)]
        
        possible_friendships = []
        for user_id in self.users:
            # To prevent duplicate friendships create from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                # if friendship between user_id and user_id_2 already exists
                    # don't add friendship between user_id_2 and user_id
                possible_friendships.append((user_id, friend_id))
        # Randomly selected X friendships 
        # the formula for X is num_users * avg_friendships // 2 (divide by 2 so that the frienship is counted by 1 because they're bi-directional)
        # shuffle the array and pick X elements from the front
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            

    def get_all_social_paths(self, user_id):
        pass
    #     """
    #     Takes a user's user_id as an argument
    #     Returns a dictionary containing every user in that user's
    #     extended network with the shortest friendship path between them.
    #     The key is the friend's ID and the value is the path.
    #     """
        visited = {}  # Note that this is a dictionary, not a set
    #     # !!!! IMPLEMENT ME
    #       # create a queue
    #     queue = []
    #     # add the starting vertex to the queue initialized as a list
    #     queue.append(self.friendships[user_id])
    #     print(queue)
    #     # create a set to store visited values in it to avoide infinite loops
    #     # while vertices haven't been visited, loop (while the queue isn't empty)
    #     while len(queue) > 0:
    #         # pop off the first element in the list
    #         path = queue.pop(0)
    #         # grab the last element in the path 
    #         current_node = path[-1]
    #         # if the node isn't in visited, add it
    #         if current_node not in visited:
    #             visited.add(current_node)
    #             # if the node is the destination then return the path
    #             if current_node == destination_vertex:
    #                 return path
    #         # it is not the destination so grab that node's neighbors 
    #         neigh = self.get_neighbors(current_node)
    #         # loop through the node's neighbors since these are a set 
    #         for n in neigh:
    #             new = list(path)
    #             new.append(n)
    #             queue.append(new)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.add_user("Artem")
    sg.add_user("Alice")
    sg.add_user("bob")
    sg.populate_graph(5, 2)
    print(sg.friendships)
    #connections = sg.get_all_social_paths(1)
    #print(connections)
