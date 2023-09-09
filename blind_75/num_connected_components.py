# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
"""
Notes: 
from nodes 1 to n
   if node has been visited - ignore
   perform a dfs and mark a states hash map with VISITED states to visit all connected components
   with each DFS increment count

Post interview evaluation: 
   start 9:03 to 9:33am - 30 minutes
   Good - Ended up with a working solution. Walked through several edge cases. Talked out loud most of the time. I also used the drawing feature on coderpad to simulate 
   how I would draw in a real interview. 
   Needs Improvement - Tried to apply union find algo (I remembered from practice that it was possible to use that algo here) but I couldn't remember the algorithm. 
   I ended up just going through what happens if you just mark each connected component and found that a DFS or BFS would work in this case.


"""

UNVISITED = 0
VISITING = 1
VISITED = 2
def dfs(n, graph, states):
    # get edges
    for neighbor in graph[n]:
        if states[neighbor] == VISITING or  states[neighbor] == VISITED:
            continue
        states[neighbor] = VISITING
        dfs(neighbor, graph, states)
        states[neighbor] = VISITED
    
def num_connected_components(n, edges):
    num_connected = 0
    states = {v: UNVISITED for v in range(n)}
    # build graph
    graph = {vertice: set() for vertice in range(n)}
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    for num in range(n):
        if states[num] == VISITED:
            continue
        states[num] = VISITING
        dfs(num, graph, states)
        states[num] = VISITED
        num_connected += 1
    return num_connected

assert num_connected_components(5, [[0,1],[1,2],[3,4]]) == 2
assert num_connected_components(5, [[0,1],[1,2],[2,3],[3,4]]) == 1
assert num_connected_components(5, []) == 5
assert num_connected_components(2, [[1,0]]) == 1


    


   
    
