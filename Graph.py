import sys
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

max = sys.maxsize

plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

def ehCompleto(self):
  if (arresta == no*(no-1)/2):
    return True
  else:
    return False

def buscaLargura(G,busca):
  visitado = set()
  caminho = []
  fila = [busca]
  while fila:
    no = fila.pop(0)
    visitado.add(no)
    caminho.append(no)
    for vizinho in G[no]:
      if vizinho in visitado:
        continue
  fila.append(vizinho)  
buscaLargura(G, 0)

def buscaProfundidade(G, busca):
  caminho = []
  pilha = [busca]
  while(len(pilha) != 0):
    i = pilha.pop()
    if i not in caminho:
      caminho.append(i)
    if i not in G:
      continue
    for vizinho in G[i]:
      pilha.append(vizinho)
  return " ".join(caminho)
buscaProfundidade(G, 0)

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

def menorCaminho(self, distancia, passos):
        minimo = sys.maxint
        for v in range(self.no):
            if distancia[v] < minimo and passos[v] == False:
                minimo = distancia[v]
                minimo_indice = v
        return minimo_indice

def dijkstra(self, i):
  distancia = [sys.maxsize] * self.vertice
  distancia[i] = 0
  passos = [False] * self.vertice
  for cout in range(self.vertice):
    u = self.menorCaminho(distancia, passos)
    passos[u] = True
    for v in range(self.vertice):
      if self.G[u][v] > 0 and passos[v] == False and distancia[v] > distancia[u] + self.G[u][v]:
        distancia[v] = distancia[u] + self.G[u][v]
  self.printSolution(distancia)
dijkstra(0,1)