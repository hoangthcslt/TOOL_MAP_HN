def get_labeled_nodes(graph):
    return [(n, graph.nodes[n].get('label', '')) for n in graph.nodes()]