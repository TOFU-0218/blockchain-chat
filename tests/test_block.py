import hashlib

from blockchain_chat.block import Block

# ブロック生成テスト
def test_create_block():
    block = Block("Alice", "Bob", "Hello!")
    assert block.sender == "Alice"
    assert block.recipient == "Bob"
    assert block.message == "Hello!"
    assert block.before_hash == "a"
    assert block.index == 0
    time = block.timestamp
    hash_sha256 = hashlib.sha256(f"AliceBobHello!{time}a0".encode())
    assert block.hash == hash_sha256.hexdigest()
    assert block.block == {
        "sender": "Alice",
        "recipient": "Bob",
        "message": "Hello!",
        "timestamp": time,
        "before_hash": "a",
        "index": 0,
        "hash": hash_sha256.hexdigest()
    }