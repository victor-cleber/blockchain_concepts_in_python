from blockchain.Block import Block

blockchain = []

genesis_block = Block("Chacellor on the brink...", ["Satoshi sent 1 BTC to Victor",
                                                    "Maria sent 5 BTC to Jenny",
                                                    "Satoshi sent 5 BTC to Hal Finney"])
second_block = Block(genesis_block.block_hash, ["Ivan sent 1 BTC to Jhonn",
                                            "Maria sent 5 BTC to Ivan",
                                            "Satoshi sent 5 BTC to Victor"])

third_block = Block(second_block.block_hash, ["A to C 5 BTC","B to D 5 BTC"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)
print("Block hash: Second Block")
print(second_block.block_hash)
print("Block hash: Third Block")
print(third_block.block_hash)


