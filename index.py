import hashlib

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, block_data, block_hash, prev_hash):
        self.data = block_data
        self.hash = block_hash
        self.prevHash = prev_hash

    def __str__(self):
        return f"Data: {self.data}, Hash: {self.hash}, PrevHash: {self.prevHash}"

class Blockchain:
    def __init__(self):
        hashLast = hashGenerator("last_gen")
        hashFirst = hashGenerator("first_gen")
        
        genesis = Block("gen_data", hashFirst, hashLast)
        self.chain = [genesis]

    def addBlock(self, data):
        prevHash = self.chain[-1].hash
        blockHash = hashGenerator(data + prevHash)
        block = Block(data, blockHash, prevHash)
        self.chain.append(block)

blch = Blockchain()
blch.addBlock('A')
blch.addBlock('B')
blch.addBlock('C')

for block in blch.chain:
    print(block)
