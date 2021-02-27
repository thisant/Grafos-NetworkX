import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('A'), ('B'), ('C'), ('D'), ('E')

G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('D','E')
G.add_edge('E','A')
G.add_edge('B','E')

plt.figure(5)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()