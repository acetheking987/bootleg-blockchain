import block, random, file_handler
from colorama import Fore

open('blockchain.txt', 'w').close()
file = file_handler.file_handler("blockchain.json")
difficulty = 5
tries = []

while True:
    data = file.read_file()

    if len(data) == 0:
        prev_hash = '0'
        id = 0
    else:
        prev_hash = data[-1]["block_hash"]
        id = data[-1]["block_id"] + 1

    block_data = ""
    for i in range(0, random.randint(10, 100)):
        block_data += str(random.randint(1, 1000))

    current_block = block.Block(id, block_data, prev_hash, difficulty)
    current_block.thread_mine_block()
    current_block.dispaly_block()
    tries.append(current_block.tries)
    avg_tries = sum(tries) / len(tries)
    print(f"{Fore.RED}Avg Tries: {Fore.BLUE}{avg_tries}{Fore.RESET}\n{Fore.RED}Tries: {Fore.BLUE}{current_block.tries}{Fore.RESET}\n{Fore.RED}Difficulty: {Fore.BLUE}{difficulty}{Fore.RESET}\n{Fore.RED}sucessful_thread_id: {Fore.BLUE}{current_block.sucessful_thread_id}{Fore.RESET}\n")
    dict_block = current_block.to_dict()
    dict_block["avg_tries"] = avg_tries
    data.append(dict_block)
    file.write_file(data)