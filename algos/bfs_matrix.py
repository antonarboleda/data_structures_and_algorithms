
def get_neighbors(coord, N, M):
    row, col = coord
    delta_row = [-1,0,1,0]
    delta_col = [0,1,0,-1]
    result = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = row + delta_col[i]
        if 0 <= neighbor_row < N and 0 <= neighbor_col < N:
            result.append((neighbor_row, neighbor_col))
    return result
import collections

def matrix_bfs(start_node):
    queue = collections.deque([start_node])
    visited = set([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            # do stuff with node if required
            queue.append(neighbor)
            visited.add(neighbor)