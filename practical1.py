from queue import Queue

romaniaMap = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
     'Neamt': ['Iasi']
}

def bfs(startingNode, destinationNode):
    visited = {}
    parent = {}
    queue = Queue()

    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None

    startingCity = startingNode
    visited[startingCity] = True
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()

        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)

    path = []
    g = destinationNode
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    return path

shortest_path = bfs('Arad', 'Bucharest')
print(shortest_path)
