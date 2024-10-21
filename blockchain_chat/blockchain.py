import time

from blockchain_chat.block import Block

class Blockchain:
    def __init__(self):
        self.chain = {}

    def add_block(self, sender, recipient, message):
        if len(self.chain) == 0:
            previous_hash = "genesis"
        else:
            previous_hash = list(self.chain.values())[-1].hash
        index = len(self.chain)
        timestamp = time.time()
        block = Block(sender, recipient, message, timestamp, previous_hash, index)
        self.chain[index] = block
