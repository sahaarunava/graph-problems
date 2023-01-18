import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def select_random_numbers_within_range(start: int,
                                       end:   int,
                                       n:     int):
    """Return n random numbers within [start, end]

    Args:
        start (int): _description_
        end (int): _description_
        n (int): _description_

    Returns:
        _type_: _description_
    """
    res = []
    for j in range(n):
        res.append(np.random.randint(start, end))
    return res

d = 5
num_nodes = 10
k = 5
random_graph = nx.random_regular_graph(d=d, n=num_nodes)
# random_graph = nx.gn_graph(n=num_nodes)
nx.draw(random_graph)
plt.savefig("graph.png")
nx.write_adjlist(random_graph, "graph.adjlist")

# Generate random start/end point list
start_points = select_random_numbers_within_range(start=0, end=num_nodes, n=k)
end_points = select_random_numbers_within_range(start=0, end=num_nodes, n=k)
dict = {"start": start_points, "end": end_points}
df = pd.DataFrame(dict)
df.to_csv("start_end_list.csv", index=False)

print(random_graph)
print(nx.shortest_path(random_graph, 1, 5))


# print(random_graph.nodes)
# print(nx.node_connectivity(random_graph, 2, 78))
# print(nx.node_connectivity(random_graph, 1, 0))
# print(nx.node_connectivity(random_graph, 2, 0))
# print(nx.shortest_path(random_graph, 3, 0))
# # This will throw exception as disconnected
# print(nx.shortest_path(random_graph, 2, 78))