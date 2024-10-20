import hashlib, time

class Block:
    def __init__(self, sender, recipient, message, before_hash = "a", before_index = -1):
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.timestamp = time.time()
        self.before_hash = before_hash
        self.index = before_index + 1
        self.hash = hashlib.sha256(f"{self.sender}{self.recipient}{self.message}{self.timestamp}{self.before_hash}{self.index}".encode()).hexdigest()
        self.block = {
            "sender": self.sender,
            "recipient": self.recipient,
            "message": self.message,
            "timestamp": self.timestamp,
            "before_hash": self.before_hash,
            "index": self.index,
            "hash": self.hash
        }