from hashlib import sha256
import json

class block:
    # Medoto constructor
    def __init__(self, index, transaccion, marcaDeTiempo):
        self.index = index
        self.transaccion = transaccion
        self.marcaDeTiempo = marcaDeTiempo
        
    def compute_hash(block):
        block_string = json.dumps(self.__dict__,sort = True)
        return sha256(block_string.encode()).hexdigest()
        
class Blockchain:
    # metodo constructor
    def __init__(self):
        self.unconfirmed_trasactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block():
        genesis_block = Block(, [], time.time(), "0"*64)