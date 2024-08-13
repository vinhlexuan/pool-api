import json

file_path = './data.json'

def load_data() -> dict:
    with open(file_path, 'r') as f:
        loaded_pools = json.load(f)
    return loaded_pools

def save_data(pools: dict):
    with open(file_path, 'w') as f:
        json.dump(pools, f)
