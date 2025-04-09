import networkx as nx
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

def build_graph(nodes, edges):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node['id'], pos=(node['x'], node['y']), label=node.get('label', ''))

    for edge in edges:
        src, dest = edge['from'], edge['to']
        weight = euclidean_distance(
            next(n for n in nodes if n['id'] == src),
            next(n for n in nodes if n['id'] == dest)
        )
        G.add_edge(src, dest, weight=weight)
    return G