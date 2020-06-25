
from math import factorial
"""
Fill in all #TODO's
"""

def binomial(n: int, r: int) -> int:
    """
    Binomial coefficient, nCr, aka the "choose" function
    n! / (r! * (n - r)!)
    """
    if 0>r or n<r:
        return 0
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def permutations(S:list)-> list:
    """
    Generates all permutations of the input list S
    @input : a list of elements S
    @output : a list of all permutations of the list S
    """
    P = permutation_helper(S)
    assert len(P)==factorial(len(S))
    return P

def permutation_helper(S: list) -> list:
    #TODO
    pass

def powerset(S: list) -> list:
    """
    Returns the powerset of the input list S
    @input : a list of elements S
    @output : the powerset of S
    """
    P_S = powerset_helper(S)
    assert len(P_S)==2**len(S)
    return P_S
    
def powerset_helper(S: list) -> list:
    #TODO
    pass

def subsets(S: list, k: int) -> list:
    """
    Generates all subsets T of the list S that have 
    cardinality k. 
    
    @input : a list of elements S
    @output : a list of all subsets of S with cardinality k
    """
    if k>len(S) or k<0:
        raise Exception('must have 0<=k<=|S|, got k : ',k,'and |S|',len(S))
    T = subset_helper(S, k)
    assert len(T)==binomial(len(S),k)
    return T

def subset_helper(S: list, k: int) -> list:
    #TODO
    pass

