import collections

def bfs(graph, start_node):
   
    queue = collections.deque([start_node])
    visited = {start_node}
    traversal_path = []

    print(f"Starting BFS from node: '{start_node}'")
    
    while queue:
        current_node = queue.popleft()
        traversal_path.append(current_node)
        
        print(f"  Visiting node: {current_node}")
        
        # Iterate over all neighbors of the current node
        for neighbor in graph.get(current_node, []):
            # If the neighbor has not been visited yet
            if neighbor not in visited:
                # Mark it as visited
                visited.add(neighbor)
                # Enqueue the neighbor for future processing
                queue.append(neighbor)
                print(f"    -> Adding neighbor '{neighbor}' to queue.")

    return traversal_path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'], # Note: E points to F, which is already reachable from C
    'F': ['G'],
    'G': []
}


start = 'A'


bfs_result = bfs(graph, start)

# Print the final result
print("\n--- Result ---")
print(f"Graph Adjacency List: {graph}")
print(f"BFS Traversal Order: {bfs_result}")

# Expected output: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Order ensures all nodes at distance N are visited before nodes at distance N+1.