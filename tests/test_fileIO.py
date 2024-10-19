import json

from blockchain_chat.fileIO import load_data, init_data

test_data = {
    "0":{
        "from": "Alice",
        "to": "Bob",
        "message": "Hello!",
        "time": "2020-01-01 12:00:00",
        "hash": "4c716d4cf211c7b7d2f3233c941771ad0507ea5bacf93b492766aa41ae9f720d"
    },
    "1":{
        "from": "Bob",
        "to": "Alice",
        "message": "Hi!",
        "time": "2020-01-01 12:01:00",
        "hash": "daca2e083e456dff21ff10998c1e99f414e45e5f3f0709af0b33b86df4694d19"
    }
}

# データロードテスト
def test_load_data(tmp_path):
    # 一時的なJSONファイルを作成
    json_file = tmp_path / "test_data.json"
    with json_file.open('w', encoding = 'utf-8') as f:
        json.dump(test_data, f)
    
    # 初期化関数を実行
    result = load_data(json_file)

    # 結果を検証
    assert result == test_data

# データ初期化テスト
def test_init_data(tmp_path):
    # 一時的なファイルパスを作成
    json_file = tmp_path / "test_data.json"

    # 初期化関数を実行
    init_data(json_file)

    # ファイルが作成されたか確認
    assert json_file.exists(), "JSONファイルが作成されていません。"

    # ファイルの内容を読み込み
    with json_file.open('r', encoding = 'utf-8') as f:
        data = json.load(f)

    assert data == {}, "初期化されたデータが空ではありません。"

# 既存データをオーバーライドして初期化するテスト
def test_override_data(tmp_path):
    # 一時的なJSONファイルを作成
    json_file = tmp_path / "test_data.json"
    with json_file.open('w', encoding = 'utf-8') as f:
        json.dump(test_data, f)

    # 初期化関数を実行
    init_data(json_file)

    # ファイルの内容を読み込み
    with json_file.open('r', encoding = 'utf-8') as f:
        data = json.load(f)

    assert data == {}, "初期化されたデータが空ではありません。"