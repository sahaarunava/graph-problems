import networkx as nx
import pandas as pd
import logging as log

def load_graph(filename: str):
    """_summary_

    Args:
        filename (str): _description_
    """
    graph = nx.read_adjlist(path=filename, nodetype=int)
    log.warning(f'Loading done! Details: {graph}')
    return graph
    
def load_start_end_points(filename: str):
    """_summary_

    Args:
        filename (str): _description_
    """
    df = pd.read_csv(filename)
    return df.to_dict()

def find_all_connectivity(graph_file, start_end_file):
    """_summary_

    Args:
        graph_file (_type_): _description_
        start_end_file (_type_): _description_
    """
    graph = load_graph(graph_file)
    log.debug(graph.nodes)
    start_end = load_start_end_points(start_end_file)
    start_dict = start_end["start"]
    end_dict = start_end["end"]
    n = len(start_dict)
    for i in range(n):
        start = start_dict[i]
        end = end_dict[i]
        try:
            shortest_path_len = nx.shortest_path(graph, start, end)
        except Exception as e:
            log.exception(e)
            shortest_path_len = -1
        log.warning(f"{i}: {start} -> {end} => {shortest_path_len}")
            
    
find_all_connectivity(graph_file="graph.adjlist",
                      start_end_file="start_end_list.csv")