class Edge:

    """ this class represent the edge of the graph """
    def __init__(self, s, d, w: float):
        self.__src = s
        self.__dest = d
        self.__weight = w

    def __eq__(self, other):
        if isinstance(other, Edge):
            if self.__weight == other.__weight and self.__src == other.__src and self.__dest == other.__dest:
                return True
            else:
                return False
        return False

    """ Return the id of the src node of the edge"""
    def getSrc(self) -> int:
        return self.__src

    """Return the id of the destination node of the edge"""
    def getDest(self) -> int:
        return self.__dest

    """ Return the weight of the edge """
    def getWeight(self) -> float:
        return self.__weight

    """ change the weight of the edge"""
    def setWeight(self, d: float):
        self.__weight = d


