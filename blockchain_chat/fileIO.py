import json

# jsonから辞書型にする
def load_data(json_file_path):
    with json_file_path.open('r', encoding = 'utf-8') as f:
        data = json.load(f)
    return data