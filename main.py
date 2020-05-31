from Graph import Graph
from Dijkstra import Dijkstra
from ReadDijkstraInput import ReadInput


def main():

    vertexes, edges, interval = ReadInput("input")
 

    g = Graph()
    g.addVertexes(*vertexes)
    g.addEdges(*edges)

    short_path, walk_cost = Dijkstra(g,interval[0],interval[1])

    rt = "\n  Path: "
    for i in range(len(short_path)-1):
        rt += "{} ~ ".format(short_path[i])
    rt+= "{}\n  Cost: {}\n".format(short_path[i+1],walk_cost)
    
    print(rt)
    


if "__main__" == __name__:
    main()