import tkinter as tk
from map_loader import load_map_data
from graph_builder import build_graph
from path_finder import find_shortest_path
from label_manager import get_labeled_nodes
from ui import MapApp

def main():
    nodes, edges = load_map_data('map_data.json')
    graph = build_graph(nodes, edges)

    # Tạo dictionary id -> label
    label_dict = {node['id']: node.get('label', f'N{node["id"]}') for node in nodes}
    label_name_map = {v: k for k, v in label_dict.items()}  # label -> id

    def path_callback(start_id, end_id):
        return find_shortest_path(graph, start_id, end_id)

    root = tk.Tk()
    root.title("Bản đồ thông minh")

    app = MapApp(root, graph, label_dict, path_callback)
    root.mainloop()

if __name__ == '__main__':
    main()