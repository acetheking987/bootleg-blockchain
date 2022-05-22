import block, random

prev_hash = '0'
block_chain = []
for i in range(10):
    block_data = random.randint(0, 100)
    block_id = i
    block_difficulty = 4
    test_block = block.Block(block_id, block_data, prev_hash, block_difficulty)
    test_block.mine_block()
    test_block.dispaly_block()
    prev_hash = test_block.get_hash()
    block_chain.append(test_block.to_str())
    print('')