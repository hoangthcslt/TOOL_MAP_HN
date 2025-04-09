import networkx as nx

def find_shortest_path(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return None