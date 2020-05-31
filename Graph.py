import sys 
class Graph:
    def __init__(self):
        self.vertexes = list()
        self.edges = list()


    def addEdges(self,*edges):
        self.edges.extend(edges)

    def addVertexes(self,*vertexes):
        self.vertexes.extend(vertexes)

    def getVertex(self,id_i):
        for vertex in self.vertexes:
            if (vertex.id == id_i):
                return vertex 

    def getEdge(self,id_i,id_j):
        for edge in self.edges:
            if ((edge.vertexA.id == id_i and edge.vertexB.id == id_j) or 
                (edge.vertexA.id == id_j and edge.vertexB.id == id_i)):
                return edge
    
    def getEdgesByVertex(self,id_i):
        r = list()
        for edge in self.edges:
            if(edge.vertexA.id == id_i or edge.vertexB.id == id_i):
                r.append(edge)
        return r

    def order(self):
        return len(self.vertexes)

    def size(self):
        return len(self.edges)

    def dijkstra_dict(self):
        d = dict()
        for v in self.vertexes:
            d[v.id] = {"distance":sys.maxsize,"from":None}
        return d
        