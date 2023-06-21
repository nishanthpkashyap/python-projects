class Graph:
    def __init__(self, start):
        self.start = start
        self.parent = {}
        self.status = {}
        self.solution = {}
        self.graph = graph
        self.h = heuristic

    def get_heuristic(self, n):
        return self.h.get(n, 0)

    def get_status(self, n):
        return self.status.get(n, 0)

    def get_neighbours(self, n):
        return self.graph.get(n, '')

    def print_solution(self):
        print(self.solution)

    def min_cost_child_list(self, n):
        min_cost = 0
        child_list = {min_cost: []}
        flag = True

        for i in self.get_neighbours(n):
            cost = 0
            node_list = []
            for m, weight in i:
                cost += self.get_heuristic(m) + weight
                node_list.append(m)

            if flag:
                min_cost = cost
                child_list[min_cost] = node_list
                flag = False
            else:
                if min_cost > cost:
                    min_cost = cost
                    child_list[min_cost] = node_list

        return min_cost, child_list[min_cost]

    def ao_star(self, n, back_track):
        if self.get_status(n) >= 0:
            min_cost, child_list = self.min_cost_child_list(n)
            self.h[n] = min_cost
            self.status[n] = len(child_list)
            solved = True

            for child in child_list:
                self.parent[child] = n
                if self.get_status(child) != -1:
                    solved = False

            if solved:
                self.status[n] = -1
                self.solution[n] = child_list

            if n != self.start:
                self.ao_star(self.parent[n], True)

            if not back_track:
                for child in child_list:
                    self.status[child] = 0
                    self.ao_star(child, False)


heuristic = {
    'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'G': 3, 'H': 2, 'I': 1, 'J': 0
}
graph = {
    'A': [[('B', 1), ('C', 1), ('D', 1)]],
    'B': [[('E', 1)], [('I', 1)]],
    'C': [[('F', 1)], [('I', 1)]],
    'D': [[('G', 1)], [('I', 1)]],
    'I': [[('J', 1)]],
}

g = Graph('A')
g.ao_star('A', False)
g.print_solution()
