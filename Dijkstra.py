import sys
def Dijkstra(graph,id_i,id_j):
    vertexes = graph.vertexes
    dk_dict = graph.dijkstra_dict()
    dk_dict[id_i]["distance"] = 0
    dk_dict[id_i]["from"] = id_i
    while vertexes: 
        close_v = None
        min_weight = sys.maxsize
        for v in vertexes:
            if(dk_dict[v.id]["distance"] < min_weight):
                close_v = v
        vertexes.remove(close_v)
        for edge in graph.getEdgesByVertex(close_v.id):
            vNeighbour = edge.getNeighbourOf(close_v.id)
            if(dk_dict[vNeighbour.id]["distance"] > dk_dict[close_v.id]["distance"]+edge.weight):
                dk_dict[vNeighbour.id]["distance"] = dk_dict[close_v.id]["distance"]+edge.weight
                dk_dict[vNeighbour.id]["from"] = close_v.id
                
    start = id_j
    short_path = [start] 
    while start != id_i:
        start = dk_dict[start]["from"] 
        short_path.append(start)
    short_path.reverse()
    return short_path, dk_dict[id_j]["distance"]
    
        


    
            
        








        





    

     