import hashlib

class Block:
    def __init__(self, sender, receiver, message, timestamp, previous_hash, index):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.index = index
        self.hash = self.calculate_hash()
        self.block = {
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message,
            "timestamp": self.timestamp,
            "index": self.index,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    def calculate_hash(self):
        return hashlib.sha256(f"{self.sender}{self.receiver}{self.message}{self.timestamp}{self.previous_hash}{self.index}".encode()).hexdigest()