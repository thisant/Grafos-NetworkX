import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0), (1), (2), (3), (4)

no = G.number_of_nodes()

G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,0)
G.add_edge(1,4)

arresta = G.number_of_edges()

plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

def ehCompleto(self):
  if (arresta == no*(no-1)/2):
    return True
  else:
    return False

def buscaProfundidade(G, v, visitado):
    visitado[v] = True
    for u in arresta[v]:
        if not visitado[u]:
            buscaProfundidade(G, u, visitado)

def ehConexo(self):
  for i in range(no):
    visitado = [False] * no
    buscaProfundidade(G, i, visitado)
    for b in visitado:
      if not b:
        return False
  return True

def ehRegular(self):  
  lista= list(G.degree([0, 1, 2, 3, 4]))
  grau = [indice [1] for indice in lista]
  resultado = False;
  if len(grau) > 0 :
    resultado = all(item == grau[0] for item in list1)
  if resultado:
    return True
  else:        
    return False