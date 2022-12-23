from re import T

from bibgrafo.grafo_errors import VerticeInvalidoError

from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from math import inf

class MeuGrafo(GrafoListaAdjacencia):


    def adjacentes(self, V):
        adj = []
        for a in self.arestas:
            # Check if the first vertex of the edge is the given vertex
            if a.v1 == V:
                adj.append((a.v2, a.peso))
            # Check if the second vertex of the edge is the given vertex and the graph is undirected
            elif a.v2 == V and not self.direcionado:
                adj.append((a.v1, a.peso))
        return adj

    def direcionado(self):
        '''
        Verifica se o grafo é direcionado.
        :return: Um valor booleano que indica se o grafo é direcionado
        '''
        return self.direcionado



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

    def dfs(self, V=' '):

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


    def bfs(self, V=' '):

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


    def prim(self,):
        prim = MeuGrafo()
        teste=self.ordena()
        test1=teste[0]
        proximo =self.arestas[test1].v1.rotulo
        visitados=[]
        prim.adiciona_vertice(proximo)
        while True:
            if len(self.vertices) == len(prim.vertices):
                break
            sobre = self.arestas_sobre_vertice(proximo)
            menor = inf
            menor_aresta = ''
            for a in sobre:
                if self.arestas[a].peso <= menor :
                    if not prim.existe_rotulo_vertice(self.oposto(proximo,self.arestas[a]) ):
                        menor_aresta = self.arestas[a]
                        menor = self.arestas[a].peso
            visitados.append(menor_aresta)
            if menor_aresta.v1.rotulo == proximo:
                proximo = menor_aresta.v2.rotulo
            else:
                proximo = menor_aresta.v1.rotulo
            if not prim.existe_rotulo_vertice(proximo):
                prim.adiciona_vertice(proximo)
                prim.adiciona_aresta(menor_aresta)

        return prim
    def oposto(self,V,a):
        if a.v1.rotulo == V:
            V = a.v2.rotulo
            return V
        else:
            V = a.v1.rotulo
            return V
    def Kruskall(self):
        arvore_kruskall = MeuGrafo()
        fila_prioridade = self.bucket_sort_kruskall()
        for v in self.vertices:
            arvore_kruskall.adiciona_vertice(v.rotulo)

        for i in range(len(fila_prioridade)):
            for a in fila_prioridade[i]:
                aresta = self.arestas[a]
                kruskall_dfs = arvore_kruskall.dfs(aresta.v1.rotulo)

                if kruskall_dfs.existe_rotulo_vertice(aresta.v1.rotulo) and kruskall_dfs.existe_rotulo_vertice(
                        aresta.v2.rotulo):
                    pass
                else:
                    arvore_kruskall.adiciona_aresta(aresta)

        return arvore_kruskall


    def ordena(self):
            ordenada=[]
            menor=inf
            for a in self.arestas:
                if self.arestas[a].peso <= menor and not a in ordenada:
                    menor = self.arestas[a].peso
            while len(ordenada) < len(self.arestas):
                for a in self.arestas:
                    if self.arestas[a].peso== menor:
                        ordenada.append(a)
                menor+=1
            return ordenada


    def bucket_sort_kruskall(self):
        lista_pesos = []
        for a in self.arestas:
            if not self.arestas[a].peso in lista_pesos:
                lista_pesos.append(self.arestas[a].peso)
        lista_pesos.sort()
        bucket = list()
        for i in range(len(lista_pesos)):
            bucket.append([])
            for a in self.arestas:
                if self.arestas[a].peso == lista_pesos[i]:
                    bucket[i].append(a)
        return bucket