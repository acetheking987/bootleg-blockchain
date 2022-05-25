import sha, threading
from colorama import Fore

class Block():
    def __init__(self, block_id, block_data, block_prev_hash, difficulty):
        self.block_id = block_id
        self.block_data = block_data
        self.block_prev_hash = block_prev_hash
        self.difficulty = difficulty
        self.nonce = None
        self.block_hash = None
        self.threads = []
        self.complete = False
        self.tries = 0
        self.sucessful_thread_id = 0

    def mine_block(self, start_nonce=0, id=0):
        nonce = start_nonce
        while True:
            if self.complete:
                break
            self.tries += 1
            nonce += 1
            block_hash = sha.sha256(str(self.block_id) + str(self.block_data) + str(self.block_prev_hash) + str(nonce))
            if block_hash[:self.difficulty] == '0' * self.difficulty:
                self.nonce = nonce
                self.block_hash = block_hash
                self.complete = True
                self.sucessful_thread_id = id
                return True

    def thread_mine_block(self):
        for i in range(14):
            thread = threading.Thread(target=self.mine_block, args=(i * 400000, i + 1,))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()

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
            'block_hash': self.block_hash,
            'sucessful_thread_id': self.sucessful_thread_id,
            'tries': self.tries,
            'difficulty': self.difficulty
        }

def create_block(block_id, block_data, block_prev_hash, difficulty):
    block = Block(block_id, block_data, block_prev_hash, difficulty)
    block.mine_block()
    return block