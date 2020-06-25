"""
Your goal is to implement algorithms for the following three problems-

(1) Weighted Clique

(2) Backpack

(3) Longest path

You may implement these however you'd like, but please do not
modify the call signatures. It may be
convenient to add helper methods for each problem - you
are encouraged to do this and keep your code clean / readable

A graph datastructure is provided for you in
utils.datastructructures.graph.SimpleGraph

You can test your code using methods from
from assignment_1.DataGenerator (imported for you as data_generator)

For (1) use
gen_vtx_weighted_graph(n: int, p=0.5, mn=0, mx=1, directed=False) -> SimpleGraph:

For (2) use
gen_backpack_instance(n, capacity = 10, min_wt=0, max_wt=1,
                          min_val=0, max_val=1):

For (3) use
gen_edge_weighted_graph(n: int, p=0.5, mn=0, mx=1, directed=False) -> SimpleGraph


Examples for using the DataGenerator
and working with the graph data structure
are given in assignment_1.examples.py

You are encouraged to read the source code for more info.

"""

import assignment_1.DataGenerator as data_generator
from utils.datastructures.graph.Vertex import Vertex
from typing import List
from utils.datastructures.graph.SimpleGraph import SimpleGraph
import assignment_1.warmup as utils
from utils.datastructures.graph.WeightedVertex import WeightedVertex
from utils.datastructures.graph.WeightedEdge import WeightedEdge
import numpy as np


def max_weighted_clique(G : SimpleGraph) -> List[WeightedVertex]:
    """
    find a maximum vertex-weighted clique in a vertex weighted graph G

    :param G: the graph to find the clique in
    :return: A list of vertices constituting a largest
    vertex weighted clique in G
    """
    #TODO
    pass

def longest_path(G : SimpleGraph) -> List[WeightedEdge]:
    """
    find a maximum vertex-weighted clique in a vertex weighted graph G

    :param G: the graph to find the clique in
    :return: A list of vertices constituting a largest
    vertex weighted clique in G
    """
    #TODO
    pass

def knapsack(capacity : float, values : List[float],
             weights : List[float]) -> List[int]:
    """
    :param capacity: the capacity of the knapsack
    :param values: the values for each item
    :param weights: the weights for each item

    a list of integers specifying the item numbers making
    the best value knapsack given the capacity constraints
    """
    assert len(weights) == len(values)
    #TODO
    pass






