import unittest

from src.Edge import Edge


class MyTestCase(unittest.TestCase):

    def test_get_src(self):
        ed = Edge(1, 2, 12)
        self.assertTrue(ed.getSrc() == 1)

    def test_get_dest(self):
        ed = Edge(1, 2, 12)
        self.assertTrue(ed.getDest() == 2)

    def test_get_weight(self):
        ed = Edge(1, 2, 12)
        self.assertTrue(ed.getWeight() == 12)

    def test_equal(self):
        ed1 = Edge(1, 2, 12)
        ed2 = Edge(1, 2, 12)
        ed3 = Edge(6, 2, 12)
        ed4 = Edge(1, 3, 12)
        ed5 = Edge(1, 2, 12.1)
        self.assertEqual(ed1, ed2)
        self.assertNotEqual(ed1, ed3)
        self.assertNotEqual(ed1, ed4)
        self.assertNotEqual(ed1, ed5)


if __name__ == '__main__':
    unittest.main()
