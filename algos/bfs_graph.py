# Time Complexity: O(V + E)
# For an adjacenty list it would be nodes + edges
# and each edge is the vertice to item in list
# In the worst case, every edge is bidirectionally connected
# so it would be N^2
# {0: [1,2], 1: [0,2], 2:[0,1]} - 3 vertices + 6 edges

def graph_bfs(root):
    queue = deque([root])
    # initialize root in visited
    visited = set([root])
    level = 0
    while len(queue) > 0:
        node = queue.popleft()
        # here you have access to the level that you're on
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.append(neigbor)
        # here you have access to the level that you're on too
        level += 1