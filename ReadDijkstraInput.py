from Vertex import Vertex
from Edge import Edge

def ReadInput(filename):
    vertexes = list()
    edges    = list()
    interval = list()
    with open("{}.txt".format(filename),"r") as file:
        fileByRows = file.read().split("\n")
        order = int(fileByRows[0])

        for letter in fileByRows[1]: #Vertexes ID
            if(letter.isupper()):
                vertexes.append(letter)

        for letter in fileByRows[2]: # A~J
            if(letter.isupper()):
                interval.append(letter) 


        for row_i in range(3,len(fileByRows)):
            edges.append(fileByRows[row_i].split(" "))  
            for _ in range(edges[row_i-3].count("")):
                edges[row_i-3].remove('')                                                                                              
            edges[row_i-3] = [[vertexes[row_i-3],vertexes[column_i],int(edges[row_i-3][column_i])] for column_i in range(order) if edges[row_i-3][column_i].isnumeric() and edges[row_i-3][column_i] is not "0" ]
        counter = 0
        edges2 = list()
        result = list()
        edges = str(edges)
        num = str()
        for index in range(len(edges)):
            if(edges[index].isalpha() and (counter==0 or counter==1)):
                result.append(edges[index])
                counter+=1
            elif (edges[index].isnumeric() and counter==2): 
                num += edges[index]  
                if(edges[index+1].isnumeric()):
                    num += edges[index+1]
                result.append(int(num))
                counter+=1
                index+=1
                num = str()
            if(counter==3):
                edges2.append( result )
                result = list()
                counter=0
        edges = edges2
        file.close()

    ##  LISTA LIMPIA
    index = 0
    for i in edges:
        for j in edges:
            if i[0] in j  and i[1] in j and i[0]!=j[0]:
                edges.pop(index)
        index += 1   

    vertexes2 = vertexes.copy()
    vertexes = [Vertex(v_id) for v_id in vertexes] 
    edges = [Edge(vertexes[vertexes2.index(edge[0])],vertexes[vertexes2.index(edge[1])],edge[2]) for edge in edges ]        

    return vertexes, edges, interval
                 
            


                