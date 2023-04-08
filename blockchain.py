from hashlib import sha256
import json
from time import time
from datetime import datetime
from block import Block


class Transaction:
    def __init__(self, sender_address, recipient_address, value):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.value = value
    
    def to_dict(self):
        return {
            'sender_address': self.sender_address,
            'recipient_address': self.recipient_address,
            'value': self.value
        }


class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_str = json.dumps([t.to_dict() for t in self.transactions])
        block_str = f'{self.timestamp}{transactions_str}{self.previous_hash}{self.nonce}'.encode('utf-8')
        return sha256(block_str).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f'Block mined: {self.hash}')

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }

    @staticmethod
    def genesis():
        return Block(datetime.now(), [Transaction('', '', 0)])
    
def create_wallet():
    """
    Crea una billetera y devuelve la dirección pública y la clave privada.
    """
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = '04' + vk.to_string().hex()
    private_key = sk.to_string().hex()
    return public_key, private_key



class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]
        self.mining_reward = 1000
        self.difficulty = 2
        self.pending_transactions = []
        self.max_supply = 10000000000

    def create_genesis_block(self):
        return Block(datetime.now(), [Transaction('', '', 0)])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        self.chain.append(block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender_address == address:
                    balance -= transaction.value
                elif transaction.recipient_address == address:
                    balance += transaction.value
        return balance

    def mine_pending_transactions(self, miner_address):
        block = Block(datetime.now(), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        self.add_block(block)
        self.pending_transactions = [Transaction('', miner_address, 1)]

    def to_dict(self):
        return {
            'chain': [block.to_dict() for block in self.chain],
            'pending_transactions': [tx.to_dict() for tx in self.pending_transactions],
            'mining_reward': self.mining_reward,
            'difficulty': self.difficulty
        }
def print_blocks(self):
        for block in self.blocks:
            print("Block Hash:", block.hash)
            print("Block Data:", block.data)
            print("Block Nonce:", block.nonce)
            print("Block Previous Hash:", block.previous_hash)
            print("Block Timestamp:", block.timestamp)
            print("---------------")

if __name__ == '__main__':
    blockchain = Blockchain()

    transaction1 = Transaction('address1', 'address2', 50)
    transaction2 = Transaction('address2', 'address1', 25)

    blockchain.add_transaction(transaction1)
    blockchain.add_transaction(transaction2)

    blockchain.mine_pending_transactions('miners-address')

    print('\nBalance of address1:', blockchain.get_balance('address1'))
    print('Balance of address2:', blockchain.get_balance('address2'))
    print('Balance of miner:', blockchain.get_balance('miners-address'))

