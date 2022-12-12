import numpy as np
import networkx as nx
import sys

H = np.array([[*x.strip()] for x in open(sys.argv[1])])
S = tuple(*np.argwhere(H=='S'))
H[S] = 'a'
E = tuple(*np.argwhere(H=='E'))
H[E] = 'z'

G = nx.grid_2d_graph(*H.shape, create_using=nx.DiGraph)
G.remove_edges_from([(a,b) for a,b in G.edges if ord(H[b]) > ord(H[a]) + 1])

p = nx.shortest_path_length(G, target=E)
print(p[S], min(p[a] for a in p if H[a]=='a'))