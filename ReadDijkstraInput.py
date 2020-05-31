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
    

    for element in edges:
        for index in range(len(edges)):
            if(len(edges) == index):
                break
            if(element.count(element[0]) ==  edges[index].count(element[0]) and element.count(element[1]) ==  edges[index].count(element[1])):
                edges.pop(index)
                
    print(edges)
    vertexes = [Vertex(v_id) for v_id in vertexes]
    edges = [Edge(edge[0],edge[1],edge[2]) for row in edges for edge in row ]
    return vertexes, edges, interval
                 
            


                