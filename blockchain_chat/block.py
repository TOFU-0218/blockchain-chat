import hashlib, time

class Block:
    def __init__(self, sender, recipient, message, previous_hash, index):
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.index = index
        self.hash = self.calculate_hash()
        self.block = {
            "sender": self.sender,
            "recipient": self.recipient,
            "message": self.message,
            "timestamp": self.timestamp,
            "index": self.index,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    def calculate_hash(self):
        return hashlib.sha256(f"{self.sender}{self.recipient}{self.message}{self.timestamp}{self.previous_hash}{self.index}".encode()).hexdigest()