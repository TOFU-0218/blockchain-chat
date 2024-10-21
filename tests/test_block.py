import hashlib, time

from blockchain_chat.block import Block

# ブロック生成テスト
def test_create_block():
    timestamp = time.time()
    block = Block("Alice", "Bob", "Hello!", timestamp, "a", 0)
    hash_sha256 = hashlib.sha256(f"AliceBobHello!{timestamp}a0".encode())
    assert block.hash == hash_sha256.hexdigest()
    assert block.block == {
        "sender": "Alice",
        "recipient": "Bob",
        "message": "Hello!",
        "timestamp": timestamp,
        "previous_hash": "a",
        "index": 0,
        "hash": hash_sha256.hexdigest()
    }