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

aresta = G.number_of_edges()

plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

def ehCompleto(self):
  if (aresta == no*(no-1)/2):
    return True
  else:
    return False

def buscaProfundidadeConexo(G, v, visitado):
    visitado[v] = True
    for u in aresta[v]:
        if not visitado[u]:
            buscaProfundidadeConexo(G, u, visitado)

def ehConexo(self):
  for i in range(no):
    visitado = [False] * no
    buscaProfundidadeConexo(G, i, visitado)
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

def buscaProfundidade(self, busca):
  visitado = [False] * (max(self.G) + 1)
  fila = []
  fila.append(busca)
  visitado[busca] = True
  while fila:
    s = fila.pop(0)
    print (busca, fim = " ")
    for i in self.G[s]:
      if visitado[i] == False:
        fila.append(i)
        visitado[i] = True
buscaProfundidade(0,1)

def buscaLargura(self,busca):            
        visitado = [False for i in range(self.no)]
        pilha = []
        pilha.append(busca)
        while (len(pilha)):
            s = pilha[-1]
            pilha.pop()
            if (not visitado[busca]):
                print(busca,fim=' ')
                visitado[busca] = True
            for vertice in self.adj[busca]:
                if (not visitado[vertice]):
                    pilha.append(vertice)
buscaLargura(0,1)

def menorCaminho(self, distancia, sptSet):
        minimo = sys.maxint
        for v in range(self.no):
            if distancia[v] < minimo and sptSet[v] == False:
                minimo = distancia[v]
                minimo_indice = v
        return minimo_indice

def dijkstra(self, src):
  distancia = [sys.maxint] * self.no
  distancia[src] = 0
  sptSet = [False] * self.V
  for cout in range(self.no):
    u = self.menorCaminho(distancia, sptSet)
    sptSet[u] = True
    for v in range(self.V):
      if self.G[u][v] > 0 and sptSet[v] == False and \
      distancia[v] > distancia[u] + self.G[u][v]:
        distancia[v] = distancia[u] + self.G[u][v]
  self.printSolution(distancia)
dijkstra(0,1)