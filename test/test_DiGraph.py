import unittest

from src.DiGraph import DiGraph

class MyTestCase(unittest.TestCase):
    def test_nodeSize(self):
        graph = DiGraph()
        ran = 10000
        for i in range(ran):
            graph.add_node(i)
        self.assertEqual(ran, graph.v_size())

    def test_edgeSize(self):
        graph = DiGraph()
        ran = 1000
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        for i in range(ran):
            if i > 3:
                graph.add_node(i)
                graph.add_edge(i, i - 1, i - 1)
                graph.add_edge(i, i - 2, i - 2)
                graph.add_edge(i, i - 3, i - 3)
                graph.add_edge(i, i - 4, i - 4)
        x = (ran - 4) * 4
        self.assertEqual(x, graph.e_size())
        for i in range(ran):
            if i > 3:
                graph.remove_edge(i, i - 1)
        y = x - (ran - 4)
        self.assertEqual(y, graph.e_size())

    def test_addNode(self):
        graph = DiGraph()
        ran = 10000
        for i in range(ran):
            b = graph.add_node(i)
            self.assertTrue(b == True)

        for j in range(ran):
            b = graph.add_node(j)
            self.assertFalse(b == True)

    def test_addEdge(self):
        graph = DiGraph()
        ran = 1000
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        for i in range(ran):
            if i > 3:
                graph.add_node(i)
                self.assertTrue(graph.add_edge(i, i - 1, i - 1))
                self.assertTrue(graph.add_edge(i, i - 2, i - 2))
                self.assertTrue(graph.add_edge(i, i - 3, i - 3))
                self.assertTrue(graph.add_edge(i, i - 4, i - 4))
        for i in range(ran):
            if i > 3:
                graph.add_node(i)
                self.assertFalse(graph.add_edge(i, i - 1, i - 1))
                self.assertFalse(graph.add_edge(i, i - 2, i - 2))
                self.assertFalse(graph.add_edge(i, i - 3, i - 3))
                self.assertFalse(graph.add_edge(i, i - 4, i - 4))

    def test_removeEdge(self):
        graph = DiGraph()
        ran = 1000
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        for i in range(ran):
            if i > 3:
                graph.add_node(i)
                graph.add_edge(i, i - 1, i - 1)
                graph.add_edge(i, i - 2, i - 2)
                graph.add_edge(i, i - 3, i - 3)
                graph.add_edge(i, i - 4, i - 4)

        for j in range(ran):
            if j > 3:
                self.assertTrue(graph.remove_edge(j, j - 2))

    def test_removeNode(self):
        graph = DiGraph()
        ran = 10000
        for i in range(ran):
            graph.add_node(i)

        for j in range(ran):
            if j % 4 == 0:
                b = graph.remove_node(j)
                self.assertTrue(b)


if __name__ == '__main__':
    unittest.main()
