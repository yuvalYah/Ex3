import random
import matplotlib.pyplot as plt
from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node

""" this class represent the directed weighted graph
    add node , add edge , get size node ,get edge size ,
    get list of nodes , get all edges out from the node id 
    get akk edges in to node id"""


class DiGraph(GraphInterface):

    def __init__(self):
        self.__Nodes = {}
        self.__Edges = {}
        self.__allInEdges = {}
        self.__maxKey = 0
        self.__nodeSize = 0
        self.__edgeSize = 0
        self.__mc = 0

    def __eq__(self, other):
        if isinstance(other, DiGraph):
            for i in self.__Nodes:
                if self.__Nodes.get(i) is not None and other.__Nodes.get(i) is not None:
                    for j in self.__Edges.get(i):
                        if self.__Edges.get(i).get(j).__eq__(other.__Edges.get(i).get(j)) is False:
                            return False
                else:
                    return False
        else:
            return False
        return True

    """ return the size of the nodes in the graph"""

    def v_size(self):
        return self.__nodeSize

    """ return the size of the edges"""

    def e_size(self):
        return self.__edgeSize

    """ return the nodes in the graph"""

    def get_all_v(self):
        return self.__Nodes

    """ return the edges in to  id node"""

    def all_in_edges_of_node(self, id1: int):
        if self.__Nodes.get(id1) is not None:  # if this is none so the id of node dosent exist in the graph
            dic = {}
            for i in range(self.__maxKey):
                if self.__allInEdges.get(id1).get(i) is not None:
                    dic.update({i: self.__allInEdges.get(id1).get(i).getWeight()})
            return dic
        return None

    """ return dictionary of the edges out from this node"""

    def all_out_edges_of_node(self, id1: int):
        if self.__Nodes.get(id1) is not None:
            dic = {}
            for i in range(self.__maxKey):
                if self.__Edges.get(id1).get(i) is not None:
                    dic.update({i: self.__Edges.get(id1).get(i).getWeight()})

            return dic
        return None

    """return the number of changes in the graph , example:
    add /remove node, add / remove edge.
    """

    def get_mc(self):
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float):
        ans = False
        if id1 != id2 and self.__Nodes.get(id1) is not None and self.__Nodes.get(id2) is not None and weight >= 0:
            if self.__Edges.get(id1).get(id2) is None:
                e = Edge(id1, id2, weight)
                self.__Edges.get(id1).update({id2: e})
                self.__allInEdges.get(id2).update({id1: e})
                self.__mc += 1
                self.__edgeSize += 1
                ans = True
            elif self.__Edges.get(id1).get(id2) is not None and self.__Edges.get(id1).get(id2).getWeight() != weight:
                self.__Edges.get(id1).get(id2).setWeight(weight)
                self.__mc += 1
                ans = True

        return ans

    """ add node to the graph, if such node exist ->return false
        if the node dosent exist -> return true"""

    def add_node(self, node_id: int, pos: tuple = None):
        if self.__Nodes.get(node_id) is None:
            node = Node(node_id)
            node.setPos(pos)

            self.__Nodes.update({node_id: node})
            self.__Edges.update({node_id: {}})
            self.__allInEdges.update({node_id: {}})
            self.__nodeSize += 1
            self.__mc += 1
            if node_id + 1 > self.__maxKey:
                self.__maxKey = node_id + 1
            return True

        return False

    """ remove node from the graph , if we removed node how dosent
        exist in the graph -> return false
        else ->return true
        """

    def remove_node(self, node_id: int):
        if self.__Nodes.get(node_id) is not None:
            for i in self.__allInEdges.get(node_id):
                del self.__Edges.get(i)[node_id]
                self.__edgeSize -= 1
            for i in self.__Edges.get(node_id):
                del self.__allInEdges.get(i)[node_id]
                self.__edgeSize -= 1

            del self.__Edges[node_id]
            del self.__allInEdges[node_id]
            del self.__Nodes[node_id]
            self.__nodeSize -= 1
            self.__mc += 1
            return True

        return False


    """ remove edge on the graph 
        if such nodes id1 and id2 dosent exist --> there no such edge
        else if id2 neighbours of id1 ->remove this edge"""


    def remove_edge(self, node_id1: int, node_id2: int):
        if self.__Nodes.get(node_id1) is not None and self.__Nodes.get(node_id2) is not None and self.__Edges.get(
                node_id1).get(node_id2) is not None:
            del self.__Edges.get(node_id1)[node_id2]
            del self.__allInEdges.get(node_id2)[node_id1]
            self.__edgeSize -= 1
            self.__mc += 1
            return True
        return False


    # max key of key node

    def max_key(self):
        return self.__maxKey

    # This help func i create to revers all the edges in the graph --> help in SCC on graph algo.
    def revers(self, graph):
        for i in range(self.max_key()):
            if self.__Nodes.get(i) is not None:
                graph.add_node(i, self.__Nodes.get(i).getPos())
        for i in self.__Nodes:
            for j in self.__Edges.get(i):
                graph.add_edge(j, i, 1)

        return

    # dfs 1
    def dfs(self, stack: list, start: int, vis: list):
        path = []
        stack.append(start)
        vis[start] = True
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for nib in self.__Edges.get(vertex):
                if vis[nib] is False:
                    stack.append(nib)
                    vis[nib] = True
        return path


    # dfs 2 not recursiv

    def non_re_dfs(self, stack, start, vis):
        path = []
        stack.append(start)
        vis[start] = True
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for nib in self.__Edges.get(vertex):
                if vis[nib] is False:
                    stack.append(nib)
        return path


    # help me to draw the graph in plot func in graph algo

    def draw_graph(self):
        allX = []  # arr of x
        allY = []  # arr of y
        str = []
        for i in self.__Nodes:
            if self.__Nodes.get(i).getPos() is not None:
                x, y, z = self.__Nodes.get(i).getPos()
                if z == 0:
                    allX.append(x)
                    allY.append(y)
                    str.append(i)
                    plt.annotate(i, (x, y), c='green')
                else:
                    x = random.randint(0, self.__nodeSize)
                    y = random.randint(0, self.__nodeSize)
                    allX.append(x)
                    allY.append(y)
                    str.append(i)
                    self.__Nodes.get(i).setPos((x, y, 1))
                    plt.annotate(i, (x, y), c='green')
            else:
                x = random.randint(0, self.__nodeSize)
                y = random.randint(0, self.__nodeSize)
                allX.append(x)
                allY.append(y)
                str.append(i)
                self.__Nodes.get(i).setPos((x, y, 1))
                plt.annotate(i, (x, y), c='green')
        # draw arrows
        for i in self.__Nodes:
            x, y, z = self.__Nodes.get(i).getPos()
            for j in self.__Edges.get(i):
                edge = self.__Edges.get(i).get(j)
                posdest = self.__Nodes.get(edge.getDest()).getPos()
                xdest, ydest, zdest = posdest
                plt.annotate("", xy=(xdest, ydest), xytext=(x, y),
                             arrowprops=dict(arrowstyle="-|>"))

        plt.scatter(allX, allY, 80, c='red')

        # title
        plt.title(f'THE GRAPH !!\nMy graph with {self.__nodeSize} nodes and {self.__edgeSize} edges')
        plt.show()


    def __repr__(self):
        return f"Graph :|V| = {self.__nodeSize} ,|E| = {self.__edgeSize} "
