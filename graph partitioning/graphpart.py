# import needed things

# set up graph
# create graph and vertices
def add_vertex(*args):
    global graph
    global vertices_no
    global vertices
    for arg in args:
        if arg in vertices:
            print("Vertex", arg, " already exists.")
        else:
            vertices_no = vertices_no + 1
            vertices.append(arg)
            if vertices_no > 1:
                for vertex in graph:
                    vertex.append(0)
            temp = []
            for i in range(vertices_no):
                temp.append(0)
            graph.append(temp)


# add edge function - for dwave, may not need weights rn
def add_edge(*args):
    global graph
    global vertices_no
    global vertices
    # check validity of v1 and v2
    for arg in args:
        print(arg)
        v1 = arg[0]
        v2 = arg[1]
        e = arg[2]
        if v1 not in vertices:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in vertices:
            print("Vertex ", v2, " does not exist.")
        # if they are valid
        else: 
            index1 = vertices.index(v1) 
            index2 = vertices.index(v2)
            graph[index1][index2] = e

# create a few specific definitions - print graph
def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], "->", vertices[j], \
                    " edge weight: ", graph[i][j])


# set up different clauses

# not sure if applicable, but a def to check if answer is valid againsts clauses



#driver code
graph = []
vertices_no = 0
vertices = []
add_vertex(1,2,3,4)
edges = [1,2,1],[1, 3, 1],[2, 3, 3],[3, 4, 4],[4, 1, 5]
add_edge(*edges)
print_graph()
print(graph)