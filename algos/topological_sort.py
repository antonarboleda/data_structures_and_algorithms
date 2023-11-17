from collections import deque
from collections import defaultdict
from typing import List
"""
Topo sort using BFS
graph = create graph with data input

get_indegrees_from_graph(graph)

for each indegree that is equal to 0, 
    add it to a queue
while q
    popleft form q
    do something with the node like add to a list or something
    get all neighbors via the graph
        subtract an indegree from the neighbor
        if the indegree == 0
            add it to the q because it's ready to be processed

"""
class BuildNode:
    def __init__(self, dependencies, val):
        self.dependencies = dependencies
        self.val = val

def get_indegrees_from_nodes(root):
    queue = deque([root])
    indegrees = {}
    visited = set()
    while queue:
        cur = queue.popleft()
        visited.add(cur.val)
        if cur.val not in indegrees:
            indegrees[cur.val] = 0
        
        indegrees[cur.val] += len(cur.dependencies)
        for dep in cur.dependencies:
            if dep.val not in visited:
                queue.append(dep)
    return indegrees


root = BuildNode(
    [
        BuildNode([], "c"), BuildNode([BuildNode([], "f")], "b")
    ], "a")
print(get_indegrees_from_nodes(root))
def get_indegrees_from_graph(graph):
    indegrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
    return indegrees
def get_dep_graph_from_node(root):
    graph = {}
    queue = deque([root])
    visited = set()
    while queue:
        cur = queue.popleft()
        visited.add(set)
        # graph[cur.val] = [c.val for c in cur.dependencies]
        for dep in cur.dependencies:
            if dep.val not in graph:
                graph[dep.val] = []
            graph[dep.val].append(cur.val)
        
        for nei in cur.dependencies:
            if nei.val not in visited:
                queue.append(nei)
    return graph

def get_bottlenecks(root) -> List[str]: 
    bottlenecks = []
    indegs = get_indegrees_from_nodes(root)
    dep_graph = get_dep_graph_from_node(root)
    queue = deque()
    build_steps = defaultdict(set)
    for char, count in indegs.items():
        if count == 0:
            queue.append((char, 0))
    while queue:
        char, build_step_num = queue.popleft()
        build_steps[build_step_num].add(char)
        if char in dep_graph:
            for nei in dep_graph[char]:
                indegs[nei] -= 1
                if indegs[nei] == 0:
                    queue.append((nei, build_step_num + 1))        
    print(build_steps, "buildsteps")
    print(indegs, "indegs")
    print(dep_graph, "dep_graph")
    for step, nodes in build_steps.items():
        if len(nodes) == 1 and list(nodes)[0] != root.val:
            bottlenecks.append(list(nodes)[0])
    return bottlenecks
print(get_bottlenecks(root), "should be b")
#   f   g
#    \  |
#    c  b
#     \ |
#      a
# def build_graph():


def get_indegrees(graph):
    indegrees = {v: 0 for v in graph.keys()}
    for node, neighbors in graph.items():
        for nei in neighbors:
            indegrees[nei] += 1
    return indegrees

def topological_sort(graph):
    indegrees = get_indegrees(graph)
    queue = deque()
    for char, count in indegrees.items():
        if count == 0:
            queue.append(char)
    
    ordering = []
    while queue:
        job = queue.popleft()
        ordering.append(job)
        for neighbor in graph[job]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    return ordering
            
 

# print(topological_sort(
#     {
#         "a": ["b", "c"],
#         "c": ["d"],
#         "b": [],
#         "d": []
#     }
# ))        
        
    