# Example Romania map
romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def iterative_dfs(graph, start, target):
    max_depth = 3
    while True:
        visited = set()
        stack = [(start, [start])]

        while stack:
            node, path = stack.pop()

            if len(path) > max_depth:
                max_depth = len(path)

            if node == target:
                return path  # Path from start to target

            if len(path) < max_depth:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited and (neighbor, path + [neighbor]) not in stack:
                        stack.append((neighbor, path + [neighbor]))

        if not stack:  # No more nodes to explore
            return None  # No path found within the current depth limit

# Example usage
start_city = 'Arad'
target_city = 'Sibiu'
path = iterative_dfs(romania_map, start_city, target_city)

if path:
    print(f"Path from {start_city} to {target_city}:")
    print(" -> ".join(path))
else:
    print(f"No path found from {start_city} to {target_city}.")
