from blockchain_chat.blockchain import Blockchain

# ブロックチェーン初期化テスト
def test_create_blockchain():
    blockchain = Blockchain()
    assert blockchain.chain == []