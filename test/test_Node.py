import unittest

from src.Node import Node


class MyTestCase(unittest.TestCase):

    def test_get_pos(self):
        id = 10
        pos = (1, 2, 0)
        node = Node(id)
        node.setPos(pos)
        x, y, z = node.getPos()
        self.assertTrue(x == 1)
        self.assertTrue(y == 2)


    def test_get_key(self):
        id = 10
        node = Node(id)
        self.assertTrue(node.getKey() == id)

    def test_get_tag(self):
        id = 10
        node = Node(id)
        node.setTag(12)
        self.assertTrue(node.getTag())

    def test_get_info(self):
        id = 10
        node = Node(id)
        node.setInfo("test of node :)")
        self.assertTrue(node.getInfo() == "test of node :)")


if __name__ == '__main__':
    unittest.main()
