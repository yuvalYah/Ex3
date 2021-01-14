import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_load(self):
        algo = GraphAlgo()
        ans = algo.load_from_json("../data/A3")
        self.assertTrue(ans)

    def test_save(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/A5")
        ans = algo.save_to_json("test_save.json")
        self.assertTrue(ans)

    def test_connected_component(self):
        d1 = DiGraph()
        d1.add_node(0, (1, 2, 0))
        d1.add_node(1, (4, 7, 0))
        d1.add_node(2, (0, 1, 4))
        d1.add_node(3, (0, 9, 8))
        d1.add_node(4, (4, 4, 0))
        d1.add_node(5, (5, 15, 0))
        d1.add_node(6, (21, 2, 0))
        d1.add_node(7, (13, 13, 0))

        d1.add_edge(0, 1, 1)
        d1.add_edge(1, 2, 2)
        d1.add_edge(2, 3, 3)
        d1.add_edge(2, 0, 3)
        d1.add_edge(3, 4, 0.5)
        d1.add_edge(4, 5, 0.5)
        d1.add_edge(4, 7, 0.5)
        d1.add_edge(5, 6, 0.5)
        d1.add_edge(6, 4, 0.5)
        d1.add_edge(6, 7, 0.5)
        d1.add_node(8, (6, 8, 0))
        d1.add_node(9, (7, 8, 0))
        d1.add_edge(8, 9, 1)
        d1.add_edge(9, 8, 1)
        d1.add_edge(8, 0, 1)
        algo = GraphAlgo(d1)
        self.assertTrue([2, 1, 0] == algo.connected_component(2))
        self.assertTrue([9, 8] == algo.connected_component(9))
        self.assertTrue([3] == algo.connected_component(3))
        self.assertTrue([7] == algo.connected_component(7))
        self.assertTrue([5, 4, 6] == algo.connected_component(5))

    def test_connected_components(self):
        d1 = DiGraph()
        d1.add_node(0, (1, 2, 0))
        d1.add_node(1, (4, 7, 0))
        d1.add_node(2, (0, 1, 4))
        d1.add_node(3, (0, 9, 8))
        d1.add_node(4, (4, 4, 0))
        d1.add_node(5, (5, 15, 0))
        d1.add_node(6, (21, 2, 0))
        d1.add_node(7, (13, 13, 0))

        d1.add_edge(0, 1, 1)
        d1.add_edge(1, 2, 2)
        d1.add_edge(2, 3, 3)
        d1.add_edge(2, 0, 3)
        d1.add_edge(3, 4, 0.5)
        d1.add_edge(4, 5, 0.5)
        d1.add_edge(4, 7, 0.5)
        d1.add_edge(5, 6, 0.5)
        d1.add_edge(6, 4, 0.5)
        d1.add_edge(6, 7, 0.5)
        d1.add_node(8, (6, 8, 0))
        d1.add_node(9, (7, 8, 0))
        d1.add_edge(8, 9, 1)
        d1.add_edge(9, 8, 1)
        d1.add_edge(8, 0, 1)
        algo = GraphAlgo(d1)
        self.assertTrue([[0, 2, 1], [3], [4, 6, 5], [7], [9, 8]] == algo.connected_components())
    def test_shortestpath(self):
        algo = GraphAlgo()
        algo.load_from_json('../data/A5')
        dist, path = algo.shortest_path(1, 7)
        self.assertTrue(dist == 2.062180280059253)
        dist, path = algo.shortest_path(47, 19)
        self.assertTrue(dist == 17.693921758901507)
        dist, path = algo.shortest_path(20, 2)
        self.assertTrue(dist == 11.51061380461898)



if __name__ == '__main__':
    unittest.main()
