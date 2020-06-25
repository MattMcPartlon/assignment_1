

from abc import ABC, abstractmethod
from utils.datastructures.graph.Vertex import Vertex
from utils.datastructures.graph.Edge import Edge
from utils.datastructures.graph.AdjSet import AdjSet


class Graph(ABC):
    def __init__(self, adj_ty = AdjSet):
        self.vertices = {}
        self.edges = []
        self.adjs = {}
        self.adj_ty = adj_ty

    def add_vertex(self, v: Vertex, *args, **kwargs):
        """

        """
        self._add_vertex(v, *args, **kwargs)
        if v not in self.vertices :
            self.vertices[v] = None
            self.adjs[v] = self.adj_ty()
            return True
        return False

    @abstractmethod
    def _add_vertex(self):
        """
        Implement as needed - will be called whenever add_edge is
        called
        """
        pass

    def add_edge(self, e: Edge, *args, **kwargs) -> None:
        (u, v) = e.get_endpoints()
        assert u in self.vertices
        assert v in self.vertices
        self._add_edge(e, *args, **kwargs)
        self.add_adjacency(u, v)
        if not e.is_directed():
            self.add_adjacency(v, u)
        self.edges.append(e)

    @abstractmethod
    def _add_edge(self):
        """
        Implement as needed - will be called whenever add_edge is
        called
        """
        pass
    
    def n(self):
        return len(self.vertices)
    
    def m(self):
        return len(self.edges)
    
    def is_connected(self):
        """
        returns true if and only if the graph 
        consists of one connected component
        """

    def get_vertices(self):
        return [v for v in self.vertices]

    def get_edges(self):
        return [e for e in self.edges]
    
    def get_neighbors(self, u):
        return self.adjs[u].get_adjacencies()
    
    def adjacentQ(self,u,v):
        return v in self.adjs[u]

    def add_adjacency(self, u, v):
        if v not in self.adjs[u]:
            self.adjs[u].add(v)
        else:
            raise Exception('adjacency from u : ', str(u), ' to v : ', str(v),
                            ' already exists!')

    

    
    
    

