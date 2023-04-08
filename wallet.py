import hashlib
import json
from time import time

class Wallet:
    wallets = {}

    @classmethod
    def generate_new_address(cls):
        new_wallet = cls()
        address = len(cls.wallets)
        cls.wallets[str(address)] = new_wallet
        return new_wallet.get_address()

    def __init__(self):
        self.private_key = hashlib.sha256(str(time()).encode()).hexdigest()
        self.public_key = hashlib.sha256(self.private_key.encode()).hexdigest()

    def sign_transaction(self, transaction):
        transaction.signature = hashlib.sha256(self.private_key.encode() + transaction.to_dict().encode()).hexdigest()

    def get_address(self):
        return hashlib.sha256(self.public_key.encode()).hexdigest()
