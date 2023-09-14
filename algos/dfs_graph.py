# Time Complexity: O(V + E)
# For an adjacenty list it would be nodes + edges
# and each edge is the vertice to item in list
# In the worst case, every edge is bidirectionally connected
# so it would be N^2
# {0: [1,2], 1: [0,2], 2:[0,1]} - 3 vertices + 6 edges

# BFS vs DFS
# BFS 
# - better for finding shortest distance between 2 vertices
# graph of an unknown or infinite size. 
# Finding connections between friends

# DFS 
# - uses less memory than BFS for WIDE graphs since BFS has to keep all nodes
# in the queue for wide graphs this can be quiet large
# - finding far away nodes from the root, e.g. looking for an exit in a maze
def dfs(root, visited):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)