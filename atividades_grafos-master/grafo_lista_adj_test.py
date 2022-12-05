import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        #Grafo paraiba teste

        self.paraiba = MeuGrafo()

        self.paraiba.adiciona_vertice("J")
        self.paraiba.adiciona_vertice("C")
        self.paraiba.adiciona_vertice("E")
        self.paraiba.adiciona_vertice("P")
        self.paraiba.adiciona_vertice("M")
        self.paraiba.adiciona_vertice("T")
        self.paraiba.adiciona_vertice("Z")

        self.paraiba.adiciona_aresta('a1', 'J', 'C')
        self.paraiba.adiciona_aresta('a2', 'C', 'E')
        self.paraiba.adiciona_aresta('a3', 'E', 'C')
        self.paraiba.adiciona_aresta('a4', 'C', 'P')
        self.paraiba.adiciona_aresta('a5', 'P', 'C')
        self.paraiba.adiciona_aresta('a6', 'C', 'T')
        self.paraiba.adiciona_aresta('a7', 'C', 'M')
        self.paraiba.adiciona_aresta('a8', 'M', 'T')
        self.paraiba.adiciona_aresta('a9', 'T', 'Z')

        #Grafo da Paraíba g_p.dfs
        self.g_p0 = MeuGrafo()
        self.g_p0.adiciona_vertice("J")
        self.g_p0.adiciona_vertice("C")
        self.g_p0.adiciona_vertice("E")
        self.g_p0.adiciona_vertice("P")
        self.g_p0.adiciona_vertice("M")
        self.g_p0.adiciona_vertice("T")
        self.g_p0.adiciona_vertice("Z")
        self.g_p0.adiciona_aresta('a1', 'J', 'C')
        self.g_p0.adiciona_aresta('a2', 'C', 'E')
        self.g_p0.adiciona_aresta('a4', 'P', 'C')
        self.g_p0.adiciona_aresta('a6', 'T', 'C')
        self.g_p0.adiciona_aresta('a8', 'M', 'T')
        self.g_p0.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba g_p00.bfs

        self.g_p00 = MeuGrafo()
        self.g_p00.adiciona_vertice("J")
        self.g_p00.adiciona_vertice("C")
        self.g_p00.adiciona_vertice("E")
        self.g_p00.adiciona_vertice("P")
        self.g_p00.adiciona_vertice("T")
        self.g_p00.adiciona_vertice("M")
        self.g_p00.adiciona_vertice("Z")
        self.g_p00.adiciona_aresta('a1', 'J', 'C')
        self.g_p00.adiciona_aresta('a2', 'C', 'E')
        self.g_p00.adiciona_aresta('a4', 'C', 'P')
        self.g_p00.adiciona_aresta('a6', 'C', 'T')
        self.g_p00.adiciona_aresta('a7', 'C', 'M')
        self.g_p00.adiciona_aresta('a9', 'T', 'Z')

        #Grafo para prim
        self.g_prm = MeuGrafo()
        self.g_prm.adiciona_vertice("A")
        self.g_prm.adiciona_vertice("B")
        self.g_prm.adiciona_vertice("C")
        self.g_prm.adiciona_vertice("D")
        self.g_prm.adiciona_vertice("E")
        self.g_prm.adiciona_vertice("F")
        self.g_prm.adiciona_vertice("G")
        self.g_prm.adiciona_vertice("H")

        self.g_prm.adiciona_aresta("k1", "A", "B", 20)
        self.g_prm.adiciona_aresta("k2", "A", "D", 80)
        self.g_prm.adiciona_aresta("k3", "A", "G", 90)
        self.g_prm.adiciona_aresta("k4", "B", "F", 10)
        self.g_prm.adiciona_aresta("k5", "C", "F", 50)
        self.g_prm.adiciona_aresta("k6", "C", "H", 20)
        self.g_prm.adiciona_aresta("k7", "D", "G", 20)
        self.g_prm.adiciona_aresta("k8", "E", "B", 50)
        self.g_prm.adiciona_aresta("k9", "E", "G", 30)
        self.g_prm.adiciona_aresta("k10", "F", "C", 10)
        self.g_prm.adiciona_aresta("k11", "F", "D", 40)
        self.g_prm.adiciona_aresta("k12", "G", "A", 20)
        self.g_prm.adiciona_aresta("k13", "G", "A", 20)
        self.g_prm.adiciona_aresta("k14", "D", "C", 10)
        self.g_prm.adiciona_aresta("k15", "C", "D", 10)


        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))



    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l2.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertFalse(self.g_d.conexo())


    def test_ha_ciclo(self):
        self.assertFalse(self.g_p.ha_ciclo())
        self.assertFalse(self.g_p_sem_paralelas.ha_ciclo())
        self.assertFalse(self.g_c.ha_ciclo())
        self.assertFalse(self.g_c2.ha_ciclo())
        self.assertFalse(self.g_c3.ha_ciclo())
        self.assertTrue(self.g_l1.ha_ciclo())
        self.assertTrue(self.g_l2.ha_ciclo())
        self.assertTrue(self.g_l3.ha_ciclo())
        self.assertTrue(self.g_l4.ha_ciclo())
        self.assertTrue(self.g_l5.ha_ciclo())


    def test_caminho(self):
        self.assertTrue(self.g_p.caminho('J', 'C'))
        self.assertTrue(self.g_p.caminho('C', 'J'))
        self.assertTrue(self.g_p.caminho('C', 'E'))
        self.assertTrue(self.g_p.caminho('E', 'C'))
        self.assertTrue(self.g_p.caminho('C', 'P'))
        self.assertTrue(self.g_p.caminho('P', 'C'))
        self.assertTrue(self.g_p.caminho('C', 'M'))
        self.assertFalse(self.g_p.caminho('Z', 'J'))
        self.assertFalse(self.g_p.caminho('J', 'Z'))
        self.assertFalse(self.g_p.caminho('Z', 'C'))
        self.assertFalse(self.g_p.caminho('C', 'Z'))
        self.assertFalse(self.g_p.caminho('Z', 'E'))


    def test_caminho_dois_vertices(self):
        self.assertEqual(self.g_p.caminho_dois_vertices('J', 'C'), ['J', 'C'])
        self.assertEqual(self.g_p.caminho_dois_vertices('C', 'J'), ['C', 'J'])
        self.assertEqual(self.g_p.caminho_dois_vertices('C', 'E'), ['C', 'E'])
        self.assertEqual(self.g_p.caminho_dois_vertices('E', 'C'), ['E', 'C'])
        self.assertEqual(self.g_p.caminho_dois_vertices('C', 'P'), ['C', 'P'])
        self.assertEqual(self.g_p.caminho_dois_vertices('P', 'C'), ['P', 'C'])
        self.assertEqual(self.g_p.caminho_dois_vertices('C', 'M'), ['C', 'M'])
        self.assertEqual(self.g_p.caminho_dois_vertices('Z', 'J'), [])
        self.assertEqual(self.g_p.caminho_dois_vertices('J', 'Z'), [])
        self.assertEqual(self.g_p.caminho_dois_vertices('Z', 'C'), [])
        self.assertEqual(self.g_p.caminho_dois_vertices('C', 'Z'), [])
        self.assertEqual(self.g_p.caminho_dois_vertices('Z', 'E'), [])

    def test_dfs(self):
        self.assertEqual(self.paraiba.dfs('J'),(self.g_p0))



    def test_bfs(self):
        self.assertEqual(self.paraiba.bfs('J'),(self.g_p00))



    def test_mst_prim(self):
        self.assertEqual(self.g_p.mst_prim(),(self.g_prm))
