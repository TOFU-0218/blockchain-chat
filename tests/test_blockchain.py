from blockchain_chat.blockchain import Blockchain

# ブロックチェーン初期化テスト
def test_create_blockchain():
    blockchain = Blockchain()
    assert blockchain.chain == {}

# ブロック追加テスト
def test_add_block():
    blockchain = Blockchain()
    blockchain.add_block("Alice", "Bob", "Hello!")
    blockchain.add_block("Bob", "Alice", "Hi!")
    assert len(blockchain.chain) == 2
    print(blockchain.chain)