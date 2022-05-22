import block, random, file_handler

file = file_handler.file_handler("blockchain.json")
difficulty = 8

while True:
    data = file.read_file()

    if len(data) == 0:
        prev_hash = '0'
        id = 0
    else:
        prev_hash = data[-1]["block_hash"]
        id = data[-1]["block_id"] + 1

    block_data = ""
    for i in range(0, random.randint(1, 10)):
        block_data += str(random.randint(1, 1000))

    current_block = block.Block(id, block_data, prev_hash, difficulty)
    current_block.mine_block()
    current_block.dispaly_block()
    print("")
    data.append(current_block.to_dict())
    file.write_file(data)