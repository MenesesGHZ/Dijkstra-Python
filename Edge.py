class Edge:
    def __init__(self,vertexA,vertexB,weight):
        self.vertexA = vertexA
        self.vertexB = vertexB
        self.weight = weight

    
    def getNeighbourOf(self,id_i):
        if(self.vertexA.id == id_i):
            return self.vertexB
        elif(self.vertexB.id == id_i):
            return self.vertexA
        return None

    def __str__(self):
        return "{}~{}.{}".format(self.vertexA.id,self.vertexB.id,self.weight)
