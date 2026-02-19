from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("\nBFS Traversal Order:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node name ({i+1}): ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start_node = input("\nEnter starting node for BFS: ")

bfs(graph, start_node)