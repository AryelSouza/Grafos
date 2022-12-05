from re import T

from bibgrafo.grafo_errors import VerticeInvalidoError
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
import sys,io
from itertools import combinations, permutations
import math
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque
import heapq
from copy import deepcopy
from math import inf

class MeuGrafo(GrafoListaAdjacencia):








    def vertices_nao_adjacentes(self):
        '''
           Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
           Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
            :return: Uma lista com os pares de vértices não adjacentes
            '''

        arestasGrafos = set()

        for a in self.arestas:
            arestaAtual = self.arestas[a]
            verticesArestas = f'{arestaAtual.v1}-{arestaAtual.v2}'
            arestasGrafos.add(verticesArestas)

        verticesNadj = set()
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                novaAresta = f'{self.vertices[i]}-{self.vertices[j]}'
                if novaAresta not in arestasGrafos and novaAresta[::-1] not in arestasGrafos:
                    verticesNadj.add(novaAresta)

        return verticesNadj








    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1==self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        g = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                g+=1
            if self.arestas[a].v2.rotulo == V:
                g+=1 
        return g

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas=set()
        for a in self.arestas:
            if self.arestas[a].v1.rotulo + '-' + self.arestas[a].v2.rotulo in arestas:
                return True
            arestas.add(self.arestas[a].v1.rotulo + '-' + self.arestas[a].v2.rotulo)
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        arestas= set()
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                arestas.add(a)
        return arestas


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for v in self.vertices:
            if self.grau(v.rotulo) != len(self.vertices)-1:
                return False
        return True

    '''def dfs(self, V=' '):

        arv_dfs = MeuGrafo()
        arv_dfs.adiciona_vertice(V)

        return self.dfs_aux_rec(V, arv_dfs)

    def dfs_aux_rec(self, V, arv_dfs):

        if len(self.vertices) == len(arv_dfs.vertices):
            return arv_dfs

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        rotulo = self.arestas_sobre_vertice(V)
        rotulos = list(rotulo)
        rotulos.sort()

        for a in rotulos:
            if not arv_dfs.existe_rotulo_vertice(a):

                if V == self.arestas[a].v1.rotulo:
                    r = self.arestas[a].v2.rotulo
                else:
                    r = self.arestas[a].v1.rotulo

                if not arv_dfs.existe_rotulo_vertice(r):
                    arv_dfs.adiciona_vertice(r)
                    arv_dfs.adiciona_aresta(self.arestas[a])

                    arv_dfs = self.dfs_aux_rec(r, arv_dfs)

        return arv_dfs
'''

    def __dfs_recursivo(self, V, arvoreDfs, verticesVisitados, verticesAdjacentes):
        '''
        Responsável por percorrer o grafo de modo recursivo
        :param V: O vértice atual
        :param dfs: Grafo que será construido pela DFS
        :param verticesVisitados: Conjunto responsável por armazenar os
        vértices já visitados durante a busca
        :param verticesAdjacentes: Lista de Adjacência do grafo
        '''
        verticesVisitados.add(V)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:

            if verticeAdjacente not in verticesVisitados:
                if not arvoreDfs.existeVertice(verticeAdjacente):
                    arvoreDfs.adicionaVertice(verticeAdjacente)
                arvoreDfs.adicionaAresta(rotuloAresta, V, verticeAdjacente)

                self.__dfs_recursivo(verticeAdjacente, arvoreDfs, verticesVisitados, verticesAdjacentes)

    def dfs(self, V=''):
        '''
        Provê um grafo gerado pela DFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''


        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        arvoreDfs = MeuGrafo([V])
        verticesVisitados = set()

        if V not in verticesAdjacentes: return arvoreDfs

        self.__dfs_recursivo(V, arvoreDfs, verticesVisitados, verticesAdjacentes)

        return arvoreDfs

    def __gerar_caminho_ciclo(self, verticeInicial, v, pai, ciclo):
        '''
        Gera de maneira recursiva a lista com o ciclo, com base no dicionário
        de vértices contendo os seus respectivos pais.
        :param verticeInicial: Vértice de partida do ciclo
        :param v: Vertice atual na chamada recursiva
        :param pai: Dicionário que armazena o vértice que era anterior a um
        vertice x no fluxo da DFS e a aresta que liga os dois vértices
        '''
        if v not in pai: return

        ciclo.append(pai[v][1])
        ciclo.append(pai[v][0])

        if verticeInicial == pai[v][0]:
            return

        self.__gerar_caminho_ciclo(verticeInicial, pai[v][0], pai, ciclo)

    def __dfs_ciclo(self, V, arestaAnterior, verticeInicio, verticesAdjacentes, visitados, pai):
        '''
        Se for possivel, responsável por encontrar um ciclo saindo do
        vértice de partida em um grafo para ele mesmo.
        :param V: Vértice atual da DFS
        :param arestaAnterior: Rótulo da aresta pelo o qual veio o vértice V
        no fluxo da DFS
        :param verticeInicio: Vértice de partida da DFS
        :param verticesAdjacentes: Dicionário com os vértices adjacentes
        de cada vértice do grafo
        :param visitados: Vértices já visitados na DFS
        :param pai: Dicionário que armazena o vértice que era anterior a um
        vertice x no fluxo da DFS e a aresta que liga os dois vértices
        '''
        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente == verticeInicio and rotuloAresta != arestaAnterior:
                pai[verticeAdjacente] = (V, rotuloAresta)
                return

            if verticeAdjacente not in visitados:
                pai[verticeAdjacente] = (V, rotuloAresta)
                visitados.add(verticeAdjacente)
                self.__dfs_ciclo(verticeAdjacente, rotuloAresta, verticeInicio, verticesAdjacentes, visitados, pai)


    '''def bfs(self, V=' '):

        arv_bfs = MeuGrafo()
        arv_bfs.adiciona_vertice(V)
        ordem = list()

        return self.bfs_aux_rec(V, arv_bfs, ordem)

    def bfs_aux_rec(self, V, arv_bfs, ordem):

        if len(self.vertices) == len(arv_bfs.vertices):
            print(ordem)
            return arv_bfs

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V and self.arestas[a].v1.rotulo != self.arestas[a].v2.rotulo:
                aux = self.arestas[a].v1.rotulo
                prox = self.arestas[a].v2.rotulo

                if arv_bfs.existe_rotulo_vertice(aux) and not arv_bfs.existe_rotulo_vertice(prox):
                    arv_bfs.adiciona_vertice(prox)
                    arv_bfs.adiciona_aresta(self.arestas[a])
                    ordem.append("{}-{}".format(self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo))
                    #self.bfs_aux_rec(prox, arv_bfs)

        self.bfs_aux_rec(prox, arv_bfs, ordem)

        return arv_bfs
'''

    def __gerarVerticesAdjacencentes(self):
        '''
        Gera dicionário com os vertices adjacentes de cada vértice do grafo
        para otimizar a realização da DFS e da BFS.
        '''
        verticesAdjacentes = {}

        for aresta in self.arestas:
            arestaAtual = self.arestas[aresta]
            #substituto  do getv1
            if arestaAtual.v1.rotulo not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.v1.rotulo] = [(arestaAtual.v2.rotulo, arestaAtual.rotulo)]
            else:
                verticesAdjacentes[arestaAtual.v1.rotulo].append((arestaAtual.v2.rotulo, arestaAtual.rotulo))

            #substituto do getv2
            if arestaAtual.v2.rotulo not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.v2.rotulo] = [(arestaAtual.v1.rotulo, arestaAtual.rotulo)]
            else:
                verticesAdjacentes[arestaAtual.v2.rotulo].append((arestaAtual.v1.rotulo, arestaAtual.rotulo))

        return


    def bfs(self, V=''):
        '''
        Provê um grafo gerado pela BFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n+m) -> n - Quantidade de vértices; m- Quantidade de arestas


        arvoreBfs = MeuGrafo([V])

        verticesVisitados = ([V])
        fila = deque([V])

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        if V not in verticesAdjacentes: return arvoreBfs

        while len(fila) != 0:
            verticeAtual = fila.popleft()

            for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[verticeAtual]:
                if verticeAdjacente not in verticesVisitados:
                    if not arvoreBfs.existe_vertice(verticeAdjacente):
                        arvoreBfs.adiciona_vertice(verticeAdjacente)

                    arvoreBfs.adiciona_aresta(rotuloAresta, verticeAtual, verticeAdjacente)

                    verticesVisitados.append(verticeAdjacente)
                    fila.append(verticeAdjacente)

        return arvoreBfs

    def ha_ciclo(self):
        '''
        Usando DFS, essa função percorre o grafo procurando por um ciclo.
        :return: uma lista no formato [v1, a1, v2, a2, v3, a3, …, an, v1]
        (onde vx são vértices e ax são arestas) indicando os vértices e arestas que formam o ciclo.
        Se não existir nenhum ciclo no grafo, ele retorna 'False'.
        '''
       


    def caminho(self,n):
        '''
        Verifica se existe um caminho entre os vértices V1 e V2.
        :param V1: O vértice de origem
        :param V2: O vértice de destino
        :return: Um valor booleano que indica se existe um caminho entre os vértices V1 e V2
        :raises: VerticeInvalidoException se um dos vértices não existe no grafo
        '''


    def conexo(self):
        '''
        Verifica se o grafo é conexo.
        :return: Um valor booleano que indica se o grafo é conexo
'''

    def caminho_dois_vertices(self, V1, V2):
        '''
        Verifica se existe um caminho entre os vértices V1 e V2.
        :param V1: O vértice de origem
        :param V2: O vértice de destino
        :return: Um valor booleano que indica se existe um caminho entre os vértices V1 e V2
        :raises: VerticeInvalidoException se um dos vértices não existe no grafo
        '''
