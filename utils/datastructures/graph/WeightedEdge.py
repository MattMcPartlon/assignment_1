import utils.datastructures.graph.Edge as Edge

class WeightedEdge(Edge.Edge):
    
    def __init__(self, u, v, weight, directed=False):
        super().__init__(u,v,weight,directed=directed)

    def get_weight(self):
        return self.data

