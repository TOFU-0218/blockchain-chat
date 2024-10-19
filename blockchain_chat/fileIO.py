import json

# jsonファイルに書き込み
def write_data(json_file_path, data):
    pass

# jsonから辞書型にする
def load_data(json_file_path):
    with json_file_path.open('r', encoding = 'utf-8') as f:
        data = json.load(f)
    return data

# jsonファイルを初期化する
def init_data(json_file_path):
    with json_file_path.open('w', encoding = 'utf-8') as f:
        json.dump({}, f)