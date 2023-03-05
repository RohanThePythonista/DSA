class AdjMatrix:
    def __init__(self, num_of_vertex):
        self.num_of_vertex = num_of_vertex
        self.matrix = [[-1] * num_of_vertex for _ in range(num_of_vertex)]
        self.adj_list = [0] * num_of_vertex
        self.vertices = {}

    def set_edge(self, frm, to, cost=0):
        f = self.vertices[frm]
        t = self.vertices[to]
        self.matrix[f][t] = cost
        self.matrix[t][f] = cost

    def set_vertex(self, vtx, _id):
        if 0 <= vtx < self.num_of_vertex:
            self.vertices[_id] = vtx
            self.adj_list[vtx] = _id

    def get_edges(self):
        edges = []
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if self.matrix[i][j] != -1:
                    edges.append((self.adj_list[i], self.adj_list[j], self.matrix[i][j]))
        return edges

    def get_vertices(self):
        return self.vertices

    def get_matrix(self):
        return self.matrix


if __name__ == '__main__':
    G = AdjMatrix(6)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    G.set_vertex(5, 'f')
    G.set_edge('a', 'e', 10)
    G.set_edge('a', 'c', 20)
    G.set_edge('c', 'b', 30)
    G.set_edge('b', 'e', 40)
    G.set_edge('e', 'd', 50)
    G.set_edge('f', 'e', 60)
    print("Vertices of Graph")
    print(G.get_vertices())
    print("Edges of Graph")
    print(G.get_edges())
    print("Adjacency Matrix of Graph")
    print(G.get_matrix())
