def a_star(start_node, stop_node):
    open_set = set(start_node)
    close_set = set()
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
                if m not in open_set and m not in close_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        parent[m] = n
                        g[m] = g[n] + weight
                        if m in close_set:
                            close_set.remove(m)
                            open_set.add(m)

        if n is None:
            print('No path exists')
            return

        if n == stop_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print(f'The path is:\n{path}\nThe cost is:\n{get_cost(path)}')
            return

        open_set.remove(n)
        close_set.add(n)

    print('No path exists')
    return


def heuristic(n):
    h = {'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'G': 3, 'H': 2, 'I': 1, 'J': 0}
    return h[n]


def get_cost(path):
    def get_dist(arr):
        for j in arr:
            if path[i + 1] == j[0]:
                return j[1]
        return 0

    dist = 0
    for i in range(len(path)-1):
        dist += get_dist(graph[path[i]])
    return dist


def get_neighbours(n):
    if n in graph:
        return graph[n]
    return None


graph = {
    'A': [('B', 6), ('F', 7)],
    'B': [('C', 5), ('D', 7)],
    'C': [('D', 1), ('E', 8)],
    'D': [('E', 6), ('C', 1)],
    'E': [('I', 5), ('J', 9)],
    'F': [('G', 9), ('H', 9)],
    'G': [('I', 8)],
    'H': [('I', 8)],
    'I': [('E', 5), ('J', 2)],
}
a_star('A', 'J')
