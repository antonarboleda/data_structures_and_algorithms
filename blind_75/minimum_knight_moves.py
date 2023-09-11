# https://leetcode.com/problems/minimum-knight-moves/
# In an infinite chess board with coordinates from -infinity to +infinity, you have 
# a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is 
# two squares in a cardinal direction, then one square in an orthogonal direction.

# Start at 8:26am  
# End time: 9:05
# Post Session Notes --- 
# I solved this one with my tests cases but when I plugged this in to the 
# LC compiler I saw a few test cases fail and it took me a while to debug 
# (probably 30 min). It's hard to dell how I would have done in an interview 
# but am happy with problem solving talking and pseudocode
"""
Pseudocode

initiate a distance matrix with all cells equal to infinity. This is 
distance from the source. distance[0][0] should be 0

BFS
use a queue and init with 0,0
remove from queue
if the node is the target, then return distance. We'll reach the target first
for all neighbors that are in bounds 
- for each neighbor check the distance hash map. If we have a closer 
to the neighbor, update it
"""
from collections import deque

def get_edges(row,col):
    return [
        (row-2, col+1), 
        (row-1,col+2), 
        (row+1,col+2), 
        (row+2,col+1), 
        (row+2, col-1), 
        (row+1,col-2), 
        (row-1,col-2), 
        (row-2,col-1)
    ]

def min_knight_moves(x: int,y: int) -> int:
    queue = deque([(0,0)])
    visited = set()
    steps = 0
    while queue:
        current_level_cnt = len(queue)
        for i in range(current_level_cnt):
            node = queue.popleft()
            row, col = node
            if row == x and col == y:
                return steps
            
            for adj_node in get_edges(row,col):
                if adj_node not in visited:
                    queue.append(adj_node)
                    visited.add(adj_node)
        steps += 1


def min_knight_moves_dfs(x,y):
    cache = {}
    def dp(x,y):
        if (x,y) in cache:
            return cache[(x,y)]
        ans = 0
        if x + y == 0: 
            ans = 0
        elif x + y == 2: 
            ans = 2
        else:
            ans = min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        cache[(x,y)] = ans
        return cache[(x,y)]
    return dp(abs(x),abs(y)) 
   
assert min_knight_moves(2,1) == 1
assert min_knight_moves(2,2) == 4
assert min_knight_moves(5,5) == 4
assert min_knight_moves_dfs(5,5) == 4
print("passed")
# [
#     [X,X,X,X,X,X]
#     [X,X,X,X,X,X]
#     [X,X,O,X,X,X]
#     [X,X,X,X,X,X]
#     [X,X,X,X,X,X]
# ]