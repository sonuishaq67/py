import networkx as nx
P=nx.path_graph(5)
Q=nx.path_graph(8)
R=nx.disjoint_union(P, Q)
#nx.draw(R)

print(nx.is_connected(R))

S=nx.star_graph(8)
nx.draw(S)
print(nx.is_connected(S))