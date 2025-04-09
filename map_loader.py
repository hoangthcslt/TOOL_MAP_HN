import json

def load_map_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data['nodes'], data['edges']