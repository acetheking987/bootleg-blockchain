import sha
from colorama import Fore


class Block():
    def __init__(self, block_id, block_data, block_prev_hash, difficulty):
        self.block_id = block_id
        self.block_data = block_data
        self.block_prev_hash = block_prev_hash
        self.difficulty = difficulty
        self.nonce = None
        self.block_hash = None

    def mine_block(self):
        nonce = 0
        while True:
            nonce += 1
            block_hash = sha.sha256(str(self.block_id) + str(self.block_data) + str(self.block_prev_hash) + str(nonce))
            if block_hash[:self.difficulty] == '0' * self.difficulty:
                self.nonce = nonce
                self.block_hash = block_hash
                return True

    def dispaly_block(self):
        print(Fore.GREEN + 'Block ID: ' + Fore.RESET + str(self.block_id))
        print(Fore.GREEN + 'Block Data: ' + Fore.RESET + str(self.block_data))
        print(Fore.GREEN + 'Block Previous Hash: ' + Fore.RESET + str(self.block_prev_hash))
        print(Fore.GREEN + 'Block Hash: ' + Fore.RESET + str(self.block_hash))
        print(Fore.GREEN + 'Nonce: ' + Fore.RESET + str(self.nonce))

    def to_str(self) -> str:
        return str(self.block_id) + str(self.block_data) + str(self.block_prev_hash) + str(self.nonce) + str(self.block_hash)

    def get_hash(self) -> str:
        return self.block_hash

    def to_dict(self) -> dict:
        return {
            'block_id': self.block_id,
            'block_data': self.block_data,
            'block_prev_hash': self.block_prev_hash,
            'nonce': self.nonce,
            'block_hash': self.block_hash
        }

def create_block(block_id, block_data, block_prev_hash, difficulty):
    block = Block(block_id, block_data, block_prev_hash, difficulty)
    block.mine_block()
    return block