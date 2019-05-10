import heapq
import numpy
import matplotlib.pyplot as pyplot

class node(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


class AStar(object):
    #maze generation
    def __init__(self):
        self.open_list = []
        heapq.heapify(self.open_list)
        self.close_list = set()
        self.nodes = []
        self.grid_height = 6
        self.grid_width = 6
        self.walls = ((0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (2, 5), (2, 3),
                 (3, 3), (4, 3), (3, 1), (5, 0), (5, 2), (5, 1))
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in self.walls:
                    reachable = False
                else:
                    reachable = True
                self.nodes.append(node(x, y, reachable))

        self.start = self.get_node(0,0)
        self.end = self.get_node(5,5)

    def get_node(self, x, y):
        return self.nodes[x * self.grid_height + y]

    def h_value_gatter(self, node):
        return 10 * (abs(node.x - self.end.x) + abs(node.y - self.end.y))

    def get_path(self):
        node = self.end
        path = [(node.x, node.y)]
        while node.parent is not self.start:
            node = node.parent
            path.append((node.x, node.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def update_node(self, adj, node):
        adj.g = node.g + 10
        adj.h = self.h_value_gatter(adj)
        adj.parent = node
        adj.f = adj.h + adj.g

    # maze solver
    def solve(self):
        heapq.heappush(self.open_list, (self.start.f, self.start))
        while len(self.open_list):
            f, node = heapq.heappop(self.open_list)
            self.close_list.add(node)
            if node is self.end:
                return self.get_path()
            adj_nodes = []
            if node.x < self.grid_width - 1:
                adj_nodes.append(self.get_node(node.x + 1, node.y))
            if node.x > 0:
                adj_nodes.append(self.get_node(node.x - 1, node.y))
            if node.y > 0:
                adj_nodes.append(self.get_node(node.x, node.y - 1))
            if node.y < self.grid_height - 1:
                adj_nodes.append(self.get_node(node.x, node.y + 1))
            for adj_node in adj_nodes:
                if adj_node.reachable and adj_node not in self.close_list:
                    if (adj_node.f, adj_node) in self.open_list:
                        if adj_node.g > node.g + 10:
                            self.update_node(adj_node, node)
                    else:
                        self.update_node(adj_node, node)
                        heapq.heappush(self.open_list, (adj_node.f, adj_node))



a_star = AStar()
a_star.solve()
print(" Solution: ")
node = a_star.end
maze_matrix = numpy.zeros((6,6))
for y in range(6):
    for x in range(6):
        maze_matrix[x,y] = -1
for i in range(6):
    for j in range(6):
        if (i, j) in a_star.walls:
            maze_matrix[i, j] = 1
maze_matrix[0,0] = 0
maze_matrix[5,5] = 0
while node.parent is not a_star.start:
    node = node.parent
    print (' node: (%d,%d)' % (node.x, node.y))
    maze_matrix[node.x, node.y] = 0
pyplot.figure(figsize=(5,3))
pyplot.imshow(maze_matrix,cmap='Greys')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()


