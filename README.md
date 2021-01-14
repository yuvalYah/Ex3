**OOP Ex3 .**
----------
I create directed weighted graph.

**Class Node :**

in class node there is key , weight , tag , info and location (of the node)

If we want to add a location to the node --> used in the setPos methode

If we want to return the id of the node , we used on getKey methode.

If we want to return the information of the node , we used on getInfo methode.

If we want to return the tag of the node , we used on getTag methode.


**Class Edge :**

in class edge there is id src , id dest , weight .

**Class DiGraph :**

This class implements directed weighted graph .

To store a list of vertices I used on dict how save the nodes

To save a list of Edges I used dict when the key is the key of the node and the value is dict of edges ,

for example: node id 0 so in Edges={0 , {{1 ,"src = 0 ,w =1, dest =1} ,{3 ,"src = 0 ,w =1, dest =3}}}
and the value is dict of Edges that the src is the key of the node.

To save edges how in to every node it's similar to Edges - its dict of edges how in to each node,

For example : in the graph has edges : 4-->0 & 3-->0 & 1-->3 so : allInEdges dict in key = 0 :
={ 0 , {4-->0 , 3-->0 , 1-->3} , 1{} ...}.

To save node size , add counter.

To save edge size add counter.

To save MC add counter.

**Class GraphAlgo :**

Implements GraphAldoInterface with Methods :

init - init the graph.

get graph.

connected component - return the list of the nodes how strongly connected .

connected components - return all the part in the graph how strongly connected with used of Tarjans algorithm.

shortest Path - get list of node_data of the shortest path between src to dest , and get the smallest distance of src to dest , with used of dijkstra algorithm.

save - save the graph with json file.

load - load the graph from json file.

plot graph- draw the graph with nodes and directed edges , if there no position to some or all node -> add random position.