import networkx as nx
import pandas as pd
import logging as log
# import argparse
import wget
# from typing import Union
from fastapi import FastAPI
import uvicorn
# from gunicorn import gunicorn
# from gunicorn.app.pasterapp import paste_server

app = FastAPI()

# parser = argparse.ArgumentParser()
# parser.add_argument("-g", "--graph", help = "Input graph")
# parser.add_argument("-s", "--start", help = "Start node")
# parser.add_argument("-f", "--end", help = "End node")
# parser.parse_args()

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

def distance(graph_file, start, end):
    """_summary_

    Args:
        graph_file (_type_): _description_
        start (_type_): _description_
        end (_type_): _description_
    """
    graph = load_graph(graph_file)
    try:
        shortest_path_len = len(nx.shortest_path(graph, start, end))
    except Exception as e:
        log.exception(e)
        shortest_path_len = -1
    log.warning(f"{start} -> {end} :: {shortest_path_len}")
    return shortest_path_len

# def find_all_connectivity(graph_file, start_end_file):
#     """_summary_

#     Args:
#         graph_file (_type_): _description_
#         start_end_file (_type_): _description_
#     """
#     graph = load_graph(graph_file)
#     log.debug(graph.nodes)
#     start_end = load_start_end_points(start_end_file)
#     start_dict = start_end["start"]
#     end_dict = start_end["end"]
#     n = len(start_dict)
#     for i in range(n):
#         start = start_dict[i]
#         end = end_dict[i]
#         try:
#             shortest_path_len = len(nx.shortest_path(graph, start, end))
#         except Exception as e:
#             log.exception(e)
#             shortest_path_len = -1
#         status = "CONNECTED" if shortest_path_len > 0 else "DISCONNECTED"
#         log.warning(f"{i}: {start} -> {end} :: {status}")
            
    
# find_all_connectivity(graph_file="../../example/1/graph.adjlist",
#                       start_end_file="../../example/1/start_end_list.csv")

# def main():
    # args = parser.parse_args()
    # g_gcs_path = args.graph
    # g_local_path = wget.download(g_gcs_path)
    # start_node = args.start
    # end_node = args.end
    # dist = distance(g_local_path, start_node, end_node)
    # log.warning(f'Dist: {dist}')
    # return dist

def get_dist(g_gcs_path, start_node, end_node):
    g_local_path = wget.download(g_gcs_path)
    dist = distance(g_local_path, start_node, end_node)
    log.warning(f'Dist: {dist}')
    return dist

@app.get("/get_distance")
def read_item(graph: str, 
              start: int,
              end: int):
    dist = get_dist(graph, start, end)
    return {"distance": dist}

if __name__ == "__main__":
    # worker_class = "uvicorn.workers.UvicornWorker"
    # paste_server(
    #     "rest_server:app",
    #     host="0.0.0.0",
    #     port="8000",
    #     workers="2",
    #     worker_class=worker_class,
    #     log_level="info",
    #     reload=True,
    # )
    uvicorn.run("main:app", workers=1, host="0.0.0.0", port=8080, log_level="info")

    
