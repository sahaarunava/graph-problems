# Problem

Given an undireted graph and a list of {start_node, end_node} pairs, print whether start_nodes are connected to the corresponding end_node.
### Input
1. The adjacency list of the graph
2. A csv containing the list of start_node, end_node pairs
### Output
Simply print `CONNECTED` iff there is a path between start_node[i] and end_node[i], `DISCONNECTED` otherwise.
### Example
#### Input
* adj list: `example/1/graph.adjlist`
* start end list: `example/1/start_end_list.csv`
#### Output
`7 -> 4 :: CONNECTED`
