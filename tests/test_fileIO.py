import json

from blockchain_chat.fileIO import load_data

# データロードテスト
def test_load_data(tmp_path):
    # テスト用のJSONデータ
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

    # 一時的なJSONファイルを作成
    json_file = tmp_path / "test_data.json"
    with json_file.open('w', encoding = 'utf-8') as f:
        json.dump(test_data, f)
    
    # 関数を実行して結果を取得
    result = load_data(json_file)

    # 結果を検証
    assert result == test_data