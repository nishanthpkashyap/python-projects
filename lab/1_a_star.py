def algo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {start_node: 0}
    parent = {start_node: start_node}

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or graph[n] is None:
            pass
        else:
            neighbours = get_neighbours(n)
            for m, weight in neighbours:
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print("No path exists")
            return None

        if n == stop_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start_node)
            path.reverse()

            print(f'\nThe Path from "{start_node}" to "{stop_node}" is:\n{path}')
            print(f'The cost is:\n{get_cost(path)}')
            return

        closed_set.add(n)
        open_set.remove(n)
    print("No path exists")
    return None


def get_cost(path):
    def get_cost_to_child(arr):
        for items in arr:
            if path[i+1] in items[0]:
                return items[1]

    dist = 0
    for i in range(len(path)):
        if path[i] in graph:
            dist += get_cost_to_child(graph[path[i]])

    return dist


def get_neighbours(n):
    if n in graph:
        return graph[n]
    return None


def heuristic(n):
    h = {'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'G': 3, 'H': 2, 'I': 1, 'J': 0}
    return h[n]


graph = {
    'A': [('B', 9), ('F', 3)],
    'B': [('C', 5), ('D', 7)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 4)],
    'F': [('G', 1), ('H', 5)],
    'G': [('I', 2)],
    'H': [('I', 1)],
    'I': [('E', 5), ('J', 2)],
}

algo('A', 'J')
