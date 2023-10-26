# Define a dictionary to represent the Romania map
romania_map = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

# Implement a basic GBFS
def gbfs(start, goal, heuristic):
    open_list = [start]
    closed_list = set()

    while open_list:
        current_city = min(open_list, key=lambda city: heuristic(city, goal))
        open_list.remove(current_city)
        closed_list.add(current_city)

        if current_city == goal:
            # Path found
            return reconstruct_path(start, goal, closed_list)

        for neighbor in romania_map[current_city]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)

    return None  # No path found

# Define a basic heuristic (straight-line distance)
def heuristic(city, goal):
    # You need to implement a real heuristic based on coordinates
    return 0

# Reconstruct the path from the goal to the start
def reconstruct_path(start, goal, closed_list):
    path = [goal]
    current_city = goal

    while current_city != start:
        for city, connections in romania_map.items():
            if current_city in connections and city in closed_list:
                path.append(city)
                current_city = city
                break

    return list(reversed(path))

# Example usage
start_city = "Arad"
goal_city = "Bucharest"

path = gbfs(start_city, goal_city, heuristic)
if path:
    print("Path:", path)
else:
    print("No path found.")
