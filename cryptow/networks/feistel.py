class PBox:
    def permute(self, block, key):
        return block

class SBox(PBox):
    def substitute(self, block, key):
        return block

class FeistelNetwork:
    def __init__(self, block_size: int, key_size: int, nrounds: int):
        self.block_size = block_size
        self.key_size = key_size
        self.nrounds = nrounds

    def subkeygen(self, key: bytes) -> bytes:
        '''
        Generates a subkey or expands a given key.
        :param key: network key of length self.key_size
        :type key: bytes
        :return: generated subkey.
        :rtype: bytes
        '''
        pass

    def round(self, state: bytes, subkey: bytes) -> bytes:
        '''
        Performs a substitution round. Also referred to as
        Feistel function (or F).
        :param state: current block state (initial block or
            previous Feistel function output)
        :type state: bytes of length self.block_size
        :return: a new state (non-permuted)
        '''
        pass

    def encrypt(self, plaintext: bytes, key: bytes):
        subkey = self.subkeygen(key)

        state = plaintext[128:] + plaintext[:128]
        for i in range(self.nrounds):
            state = state[128:] + state[:128]   # Swap left and right
            self.round(plaintext, subkey[i])    # Perform F

        return state


    def decrypt(self, cyphertext: bytes, key: bytes):
        subkey = self.subkeygen(key)

        state = plaintext[128:] + plaintext[:128]
        for i in range(self.nrounds-1, -1, -1):
            state = state[128:] + state[:128]  # Swap left and right
            self.round(plaintext, subkey[i])  # Perform F

        return state
