import networkx as nx
import matplotlib.pyplot as plt
import numpy
import itertools

def CanForce1(G,S,t,D):
  l=set([])
  for i in S:
    l.add(D[t,i])
  for j in range(1,int(max(numpy.asarray(D[t])[0])+1)):
    if j not in l:
      return True
  return False

def Done(G,S,t):
  return Done1(G,S,t,nx.floyd_warshall_numpy(G))

def Done1(G,S,t,D):
  if CanForce1(G,S,t,D):
    return False
  for v in S:
    if CanForce1(G,S,v,D):
      S.discard(v)
      return Done1(G,S,t,D)
  return True
  
def prism_graph(m):
    cycle = nx.cycle_graph(m)
    path = nx.path_graph(2)
    G = nx.cartesian_product(cycle, path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def book_graph(m):
    star = nx.star_graph(m)
    path = nx.path_graph(2)
    G = nx.cartesian_product(star, path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def stacked_book_graph(m,n):
    star = nx.star_graph(m)
    path = nx.path_graph(n)
    G = nx.cartesian_product(star, path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def hypercube_graph(m):
    path = nx.path_graph(2)
    G = nx.Graph()
    G.add_node(1)
    for i in range(m):
        G = nx.cartesian_product(G,path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def grid_graph(m,n):
    path = nx.path_graph(m)
    path2 = nx.path_graph(n)
    G = nx.cartesian_product(path,path2)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def stacked_prism_graph(m,n):
    cycle = nx.cycle_graph(m)
    path = nx.path_graph(n)
    G = nx.cartesian_product(cycle, path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def torus_graph(m,n):
    cycle = nx.cycle_graph(m)
    path = nx.cycle_graph(n)
    G = nx.cartesian_product(cycle, path)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def crown_graph(m):
    complete1 = nx.complete_graph(2)
    complete2 = nx.complete_graph(m)
    G = nx.cartesian_product(complete1,complete2)
    G = nx.convert_node_labels_to_integers(G)
    return G
    
def rook_graph(m,n):
    complete1 = nx.complete_graph(n)
    complete2 = nx.complete_graph(m)
    G = nx.cartesian_product(complete1,complete2)
    G = nx.convert_node_labels_to_integers(G)
    return G

def powerset_old(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
            
def powerset(iterable):
    items = list(iterable)
    for k in range(len(items) + 1): 
        for subset in itertools.combinations(items, k): 
            yield subset

def fd_visited(G,j):
  result=[]
  vert=list(G.nodes)
  size=len(G.nodes)+1
  vert.remove(j)
  for sub in powerset(list(vert)):
    S=set(sub)
    S.add(j)
    if len(list(S))<size:
      if Done(G,set(S),j):
        result=S
        size=len(S)
  return result
  
def fdmin(G,j):
  result=[]
  vert=list(G.nodes)
  size=len(G.nodes)+1
  vert.remove(j)
  for sub in powerset(list(vert)):
    S=set(sub)
    S.add(j) 
    if Done(G,set(S),j):
        return len(list(S))

def draw_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()