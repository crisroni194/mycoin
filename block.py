import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return "Block Hash: {}\nPrevious Hash: {}\nTimestamp: {}\nTransactions: {}\nNonce: {}".format(
            self.hash,
            self.previous_hash,
            self.timestamp,
            self.transactions,
            self.nonce
        )

    @staticmethod
    def genesis():
        return Block(0, "0", [], 1622937077.989983, 0)
