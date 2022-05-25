try:
    import block, random, file_handler, time
    from colorama import Fore

    file = file_handler.file_handler("E:\\python\\bootleg-blockchain\\blockchain.json")
    difficulty = 5
    tries = []
    times = []

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
        time_start = time.time()
        current_block.thread_mine_block()
        time_end = time.time()
        current_block.dispaly_block()
        tries.append(current_block.tries)
        times.append(time_end - time_start)
        avg_tries = sum(tries) / len(tries)
        avg_time = sum(times) / len(times)
        print(f"{Fore.RED}Avg Tries: {Fore.BLUE}{avg_tries}{Fore.RESET}\n{Fore.RED}Tries: {Fore.BLUE}{current_block.tries}{Fore.RESET}\n{Fore.RED}Difficulty: {Fore.BLUE}{difficulty}{Fore.RESET}\n{Fore.RED}sucessful_thread_id: {Fore.BLUE}{current_block.sucessful_thread_id}{Fore.RESET}\n{Fore.RED}Time: {Fore.BLUE}{round(time_end - time_start, 2)}{Fore.RESET}\n{Fore.RED}Avg Time: {Fore.BLUE}{round(avg_time, 2)}{Fore.RESET}\n")
        dict_block = current_block.to_dict()
        dict_block["avg_tries"] = avg_tries
        dict_block["time"] = round(time_end - time_start, 2)
        dict_block["avg_time"] = round(avg_time, 2)
        data.append(dict_block)
        file.write_file(data)

except Exception as e:
    input(e)