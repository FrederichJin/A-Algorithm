# graph
from graph_class import Graph
g = {'A' : ['B', 'C'],
         'B' : ['C', 'D'],
         'C' : ['D', 'A'],
         'D' : ['C', 'B'],
    }

#def generate_edges(graph):
#    edges = []
#    for node in graph:
#        for neighbour in graph[node]:
#            edges.append((node, neighbour))
#    return edges
#
#print(generate_edges(graph))
#
#def find_isolated_nodes(graph):
#    ''' return a list of isolated nodes '''
#    isolated = []
#    for node in graph:
#        if not graph[node]:
#            isolated += node
#    return isolated
#
#print(find_isolated_nodes(graph))

graph = Graph(g)
print('All path from vertex "A" to vertex "D":')
paths = graph.find_all_paths("A", "D")
print(paths)
path_len = []
shortest_path = []
for path in paths:
    path_len.append(len(path))
for path in paths:
    if len(path) == min(path_len):
        shortest_path.append(path)
print("The shortest paths are ", shortest_path)
    
        

#print('The path from vertex "A" to vertex "F":')
#path = graph.find_path("A", "F")
#print(path)
#
#print('The path from vertex "C" to vertex "C":')
#path = graph.find_path("C", "C")
#print(path)
            