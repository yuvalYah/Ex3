

class Node:
    """ This class is represent the nodes in the graph """

    def __init__(self, k: int):
        self.__key = k
        self.__info = ""
        self.__tag = 0
        self.pos = None

    """ :return the position of the node in the graph"""

    def getPos(self):
        return self.pos

    """ change the position of the node"""

    def setPos(self, set: tuple):
        self.pos = set

    """ return the key of the node """

    def getKey(self) -> int:
        return self.__key

    """return the tag of the node"""

    def getTag(self) -> int:
        return self.__tag

    """ change the tag of the node """

    def setTag(self, t: int):
        self.__tag = t

    """ return the information of the node"""

    def getInfo(self) -> str:
        return self.__info

    """ change the information of the node"""

    def setInfo(self, s: str):
        self.__info = s

