import hashlib

class SimpleCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = '-'.join(transaction_list) + '-' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


transaction_1 = 'Billy sends 1 SC to Joe'
transaction_2 = 'Bob sends 2.7 SC to Joe'
transaction_3 = 'Joe sends 3 SC to Billy'
transaction_4 = 'Dave sends 8 SC to Bob'
transaction_5 = 'Joe sends 4.3 SC to Jill'
transaction_6 = 'Billy sends 0.9 SC to Janet'

initial_block = SimpleCoinBlock('Initial Block', [transaction_1, transaction_2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = SimpleCoinBlock(initial_block.block_hash, [transaction_3, transaction_4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = SimpleCoinBlock(second_block.block_hash, [transaction_5, transaction_6])

print(third_block.block_data)
print(third_block.block_hash)