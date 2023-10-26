import heapq

# Define the Romania map as a dictionary of cities and their neighboring cities with distances.
romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101, 'Craiova': 138},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Define the heuristic (h) function using straight-line distance (as the crow flies).
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Timisoara': 329,
    'Sibiu': 253,
    'Oradea': 380,
    'Lugoj': 244,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Mehadia': 241,
    'Bucharest': 0,
    'Pitesti': 98,
    'Craiova': 160,
    'Drobeta': 242,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

def astar_search(graph, start, goal):
    # Initialize the priority queue with the starting node and a cost of 0.
    open_list = [(0, start)]
    came_from = {}
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Example: Find the shortest path from 'Arad' to 'Bucharest'.
start_city = 'Arad'
goal_city = 'Bucharest'
shortest_path = astar_search(romania_map, start_city, goal_city)

if shortest_path:
    print(f"Shortest path from {start_city} to {goal_city}:")
    print(" -> ".join(shortest_path))
else:
    print(f"No path found from {start_city} to {goal_city}.")
