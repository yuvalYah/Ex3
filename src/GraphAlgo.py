import json
from typing import List
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface

""" This class represent algorithms on graph's 
    contain : get graph, load from json , save to json
    connected component ,connected components,
    plot graph , shortest path.
    """


class GraphAlgo(GraphInterface):

    def __init__(self, g=None):
        if g is None:
            self.__algo = DiGraph()
        else:
            self.__algo = g

    """ return the graph"""

    def get_graph(self):
        return self.__algo

    """ load the graph from json file """

    def load_from_json(self, file_name: str):
        graph = DiGraph()
        try:
            with open(file_name) as json_file:
                d = json.load(json_file)
                for id, value in enumerate(d.get("Nodes")):
                    n = d.get("Nodes")[id].get("id")
                    postr = d.get("Nodes")[id].get("pos")
                    if postr is not None:
                        pos = tuple(map(float, postr.split(',')))
                        graph.add_node(n, pos)
                    else:
                        graph.add_node(n)
                for id, value in enumerate(d.get("Edges")):
                    src = d.get("Edges")[id].get("src")
                    dest = d.get("Edges")[id].get("dest")
                    w = d.get("Edges")[id].get("w")
                    graph.add_edge(src, dest, w)
                self.__algo = graph
                return True

        except Exception as e:
            print(e)
            return False

    """ save the graph to json file"""

    def save_to_json(self, file_name: str):
        try:
            with open(file_name, "w") as file:
                json.dump(self.__algo, default=lambda m: m.__dict__, indent=4, fp=file)
            return True
        except IOError as e:
            print(e)
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.__algo.get_all_v().get(id1) is not None and self.__algo.get_all_v().get(id2) is not None:
            int_vertexs = []
            doub_dist = []
            bool_vis = []
            list_arr = []

            for i in range(self.__algo.max_key()):
                if self.__algo.get_all_v().get(i) is not None:
                    int_vertexs.append(-1)
                    doub_dist.append(-1)
                    bool_vis.append(False)
                    list_arr.append([])
                else:
                    int_vertexs.append(0)
                    doub_dist.append(0)
                    bool_vis.append(True)
                    list_arr.append([])

            stack = []
            doub_dist[id1] = 0
            stack.append(id1)
            list_arr[id1] = [id1]
            while len(stack) > 0:
                ind = stack.pop(0)
                if bool_vis[id2] == True:
                    break
                if bool_vis[id2] != True:
                    for i in self.__algo.all_out_edges_of_node(ind):
                        distace = self.__algo.all_out_edges_of_node(ind).get(i) + doub_dist[ind]
                        if doub_dist[i] == -1:
                            doub_dist[i] = distace
                            int_vertexs[i] = ind
                            stack.append(i)
                            ll = list_arr[ind]
                            list_arr[i] = ll + [i]

                        elif distace < doub_dist[i]:
                            doub_dist[i] = distace
                            int_vertexs[i] = ind

                            stack.append(i)
                            ll = list_arr[ind]
                            list_arr[i] = ll + [i]

                bool_vis[ind] = True

            if len(list_arr[id2]) > 0:
                return doub_dist[id2], list_arr[id2]
            else:
                return float('inf'), []
        return float('inf'), []


    """ return the strongly connected prt of node id1
        use with dfs , and revers the graph , with Tarjans algorithm"""

    def connected_component(self, id1: int) -> list:
        if self.__algo.get_all_v().get(id1) is None:
            return []
        bool_vis_arr = []
        bool_dfs = []

        for i in range(self.__algo.max_key()):
            if self.__algo.get_all_v().get(i) is not None:
                bool_vis_arr.append(False)
                bool_dfs.append(False)
            else:
                bool_vis_arr.append(True)
                bool_dfs.append(True)
        graph = DiGraph()
        self.__algo.revers(graph)
        temp_stack = temp_stack1 = []
        temp_stack = graph.non_re_dfs(temp_stack, id1, bool_dfs)
        temp_stack1 = self.__algo.non_re_dfs(temp_stack1, id1, bool_dfs)
        temp_stack = self.__union(temp_stack, temp_stack1)

        return temp_stack

    """ return all the strongly connected parts in the graph
           use with dfs , and revers the graph , with Tarjans algorithm"""

    def connected_components(self) -> List[list]:
        bool_vis_arr = []
        bool_dfs = []
        stack = []
        f_list = []
        # init the lists
        for i in range(self.__algo.max_key()):
            if self.__algo.get_all_v().get(i) is not None:
                bool_vis_arr.append(False)
                bool_dfs.append(False)
            else:
                bool_vis_arr.append(True)
                bool_dfs.append(True)

        graph = DiGraph()
        self.__algo.revers(graph)  # revers the graph
        for i in self.__algo.get_all_v():
            if bool_vis_arr[i] is False:
                stack = self.__algo.dfs(stack, i, bool_vis_arr)

        while len(stack) > 0:
            index = stack.pop()
            temp_stack = []
            temp_stack1 = []
            if bool_dfs[index] is False:
                temp_stack = graph.non_re_dfs(temp_stack, index, bool_dfs)
                temp_stack1 = self.__algo.non_re_dfs(temp_stack1, index, bool_dfs)
                temp_stack = self.__union(temp_stack, temp_stack1)
                for k in temp_stack:
                    bool_dfs[k] = True
            f_list.append(temp_stack)
            while len(stack) > 0 and bool_dfs[stack[len(stack) - 1]] is True:
                stack.pop()
        return f_list

    """ draw the simple graph """
    def plot_graph(self) -> None:
        self.__algo.draw_graph()
        return None

    def __union(self, s1, s2):
        temp = []
        for i in s1:
            if i in s2:
                temp.append(i)
        return temp
