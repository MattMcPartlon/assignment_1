
import assignment_1.DataGenerator as dg
from utils.datastructures.graph.WeightedVertex import WeightedVertex
from utils.datastructures.graph.WeightedEdge import WeightedEdge




#generate a vertex weighted graph on 10 vertices with
# edge probability 0.5

G = dg.gen_vtx_weighted_graph(10, 0.5, mn=0, mx=5)

#access the vertices of G and print them
vertices = G.get_vertices()
print([str(v) for v in vertices])

#get the neighbors of the first vertex
v : WeightedVertex = vertices[0]
N_v = G.get_neighbors(v)

#get the weight
v.get_weight()

#get the index
v.get_idx()

#check if the first and second vertex are adjacent
u,v = vertices[0],vertices[1]
G.adjacentQ(u,v)


#generate an edge weighted graph on 10 vertices with
# edge probability 0.5

G = dg.gen_edge_weighted_graph(10, 0.5, mn=0, mx=5)

#get the edges of G and print them

edges = G.get_edges()

#print the edges
print([str(e) for e in edges])

#get the first edge and its endpoints
e : WeightedEdge = edges[0]
u,v = e.get_endpoints()
print('endpoints -- (u :',u,', v :',v,')')

#get the edge weight
e.get_weight()
