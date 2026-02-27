def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node name ({i+1}): ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors


start_node = input("\nEnter starting node for DFS: ")

visited = set()

print("\nDFS Traversal Order:")
dfs(graph, start_node, visited)