def add_node(v):  # it's work for the directed, undirected and weighted graph
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# undirected weighted graph


def add_edge(vtx1, vtx2, val):
    if vtx1 not in nodes:
        print(vtx1, "vertex 1 is not present")
    elif vtx2 not in nodes:
        print(vtx2, "vertex 2 is not present")
    else:
        index1 = nodes.index(vtx1)
        index2 = nodes.index(vtx2)
        graph[index1][index2] = val
        graph[index2][index1] = val


def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the graph")
    else:
        index1 = nodes.index(v)
        node_count = node_count-1
        nodes.remove(v)
        graph.pop(index1)   # remove row
        for i in graph:  # remove col
            i.pop(index1)


def delete_edge(vtx1, vtx2):
    if vtx1 not in nodes:
        print(vtx1, "is not present in a graph")
    elif vtx2 not in nodes:
        print(vtx2, "is not present in a graph")
    else:
        index1 = nodes.index(vtx1)
        index2 = nodes.index(vtx2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0


def print_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<2"), end=" ")
        print()


nodes = []
graph = []
node_count = 0
print("Before adding nodes:")
print(nodes)
print(graph)
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_edge("a", "b", 20)
add_edge("a", "c", 32)
delete_edge("a", "b")
print("After adding nodes:")
print(nodes)
print(graph)
print_matrix()


# undirected unweighted graph
# def add_edge(vtx1, vtx2):
#     if vtx1 not in nodes:
#         print(vtx1, "vertex 1 is not present")
#     elif vtx2 not in nodes:
#         print(vtx2, "vertex 2 is not present")
#     else:
#         index1 = nodes.index(vtx1)
#         index2 = nodes.index(vtx2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1
#
#
# directed unweighted graph
# def add_edge(vtx1, vtx2):
#     if vtx1 not in nodes:
#         print(vtx1, "vertex 1 is not present")
#     elif vtx2 not in nodes:
#         print(vtx2, "vertex 2 is not present")
#     else:
#         index1 = nodes.index(vtx1)
#         index2 = nodes.index(vtx2)
#         graph[index1][index2] = 1
#

