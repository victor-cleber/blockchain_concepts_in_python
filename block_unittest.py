import unittest
from blockchain.Block import Block

class TestBlock(unittest.TestCase):
    def test_genesis_block(self):
        genesis_block = Block("genesis transaction", ["genesis transaction"])
        self.assertEqual("46dcd5396770ce394ce0c8b259a0e6e7defb277e17bfc17ff17a51988fc9c2d2", genesis_block.block_hash)

    def test_second_block(self):
        genesis_block = Block("other genesis transaction", ["other genesis transaction"])
        second_block = Block(genesis_block.block_hash, ["second transaction"])
        self.assertEqual("bc614d0f64f95f3bebbed0fc562b5dd6dec85db07cd6c2d217936d34bb77fbe6", second_block.block_hash)

if __name__ == '__main__':
    unittest.main()
