import bibgrafo
from meu_grafo_matriz_adj_dir import *



p_t = MeuGrafo()
p_t.adiciona_vertice('A')
p_t.adiciona_vertice('B')
p_t.adiciona_vertice('C')
p_t.adiciona_vertice('D')
p_t.adiciona_vertice('E')
p_t.adiciona_vertice('F')
p_t.adiciona_aresta('a1', 'A', 'B',2)
p_t.adiciona_aresta('a2', 'A', 'C',1)
p_t.adiciona_aresta('a3', 'C', 'D',3)
p_t.adiciona_aresta('a4', 'B', 'D',1)
p_t.adiciona_aresta('a5', 'C', 'F',15)
p_t.adiciona_aresta('a6', 'D', 'E',2)
p_t.adiciona_aresta('a7', 'E', 'F',3)
p_t.dijkstra('A','F')

from math import gcd


def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
        print(m)
    return m

numeros = range(1, 8)
mmc(numeros)
