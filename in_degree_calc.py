#! /usr/bin/python

"""
This is mini project for Module 1 of Algorithmic Thinking 
course on Coursera from Rice Uni. 
The script calculates in-degree as well as in- degree dist
for digraphs represented by adjacency lists. It uses 3 test
digraphs and also introduces a funciton to generate a full graph
"""


EX_GRAPH0 = {0:set([1,2]),
             1:set(),
             2:set()}

EX_GRAPH1 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set()}

EX_GRAPH2 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3,7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1,2]),
             9:set([0,3,4,5,6,7])}



def make_complete_graph(num_nodes) :
    """ 
    Generates a full digraph ("undigraph" as well in fact) 
    with num_nodes nodes for positive num_nodes otherwise generates 
    an empty graph. Uses adjacency list format ie. dictionary. 
    """

    the_graph = {}
    if num_nodes > 0 :  
        for vert in range(num_nodes):
            edges = set(range(vert)).union(set(range(vert+1,num_nodes)))
            the_graph[vert] = edges
    return the_graph

def compute_in_degrees(digraph):
    """ computes in degrees of each node of diagraph
    returns a dictionary with indegrees of each node """
    in_degrees = {}
    for in_vert in digraph.keys():
        count = 0
        for out_vert in digraph.keys():
            #checks if node of interest in_vert is present in the adjacency list 
            #of all out_nodes but the in_vert itself, counts occurances
            if out_vert != in_vert and in_vert in digraph[out_vert]:
                count = count + 1
        in_degrees[in_vert] = count
    return in_degrees


def in_degree_distribution(digraph):
    """ computes distribution of in degrees of a digraph with aid 
    of compute_in_degree function """
    in_degr = compute_in_degrees(digraph)
    
    in_degree_dist = {}
    #uses set on the degrees to remove duplicates, sorting not needed as they 
    #will server as keys for a dictionary
    for degr in set(val for val in in_degr.values()):
        in_degree_dist[degr] = in_degr.values().count(degr) 
    
    return in_degree_dist

#print in_degree_distribution(EX_GRAPH2)
