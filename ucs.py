import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = set()

    print("\nTraversal Order:")

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(f"Visiting {node} with cost {cost}")

        visited.add(node)

        if node == goal:
            print(f"\nGoal reached! Total cost: {cost}")
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))

    print("\nGoal not reachable!")


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node name ({i+1}): ")

    m = int(input(f"Enter number of neighbors of {node}: "))

    neighbors = []

    for j in range(m):
        neighbor = input(f"Enter neighbor {j+1} name: ")
        weight = int(input(f"Enter cost to reach {neighbor}: "))
        neighbors.append((neighbor, weight))

    graph[node] = neighbors


start_node = input("\nEnter starting node: ")
goal_node = input("Enter goal node: ")

uniform_cost_search(graph, start_node, goal_node)