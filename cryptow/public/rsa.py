'''
rsa.py

RSA implementation using sympy facilities.
'''

__author__ = 'Giulio Corradini'

from random import randint
from sympy.ntheory import *
from sympy.polys import gcdex, gcd

class RSA:
    # The block size MUST be less than or equal to the
    # key size. Note: The block size is in bytes , the key size is in bits
    def __init__(self, keysize=1024):
        self.keysize = keysize
        self.ksB = keysize / 8  #keysize in bytes

    def generateprime(self):
        """
        Return a random prime number that is 'keysize' bits in size:
        :return: a random prime
        :rtype: int
        """
        return randprime(0, 2**self.keysize)

    def keysgenerator(self):
        """
        creates a public/private keys of 'keysize' bits in size:
        calculates/generates public n, e for encryption and private d for decryption
        :return: public and private keys  (e, n) (d, n)
        """
        p = self.generateprime()
        q = self.generateprime()

        n = p * q
        phi = (p-1) * (q-1)

        del p, q                #for security purposes

        e = randint(0, phi-1)
        while gcd(e, phi) != 1:
            e = randint(0, phi-1)

        dt, k1, r = gcdex(e, phi)
        d = dt % phi

        public_key = (e, n)
        private_key = (d, n)

        return public_key, private_key

    def encrypt(self, plaintext: str, pubKey):
        """
        takes plain message m, (an integer) and public key (e,n)
        calculate the cipher message c = m^e (mod n)
        :param plaintext: plaintext of size aligned to keysize!
        :param pubKey: tuple with 'e' and 'n' modulus
        :type pubKey: tuple(int, int)
        :return: ciphertext
        :rtype: bytes
        """
        e, n = pubKey

        return bytes(map(
            lambda x: pow(x, e, n).to_bytes(self.ksB),
            plaintext
        ))

    def decrypt(self, ciphertext: bytes, privKey):
        """
        takes cipher message c, (an integer) and private key (d,n)
        calculate the plain message (an integer) m = c^d (mod n)
        :param plaintext:
        :param pubKey: tuple with 'e' and 'n' modulus
        :type pubKey: tuple(int, int)
        :return: plaintext
        :rtype: bytes
        """

        d, n = privKey

        return bytes(map(
            lambda x: pow(x, d, n).to_bytes(self.ksB),
            ciphertext
        ))

    def getBlocksFromText(self, message, blockSize):
        """
        Converts a string message to a list of block integers.
        Takes the arbitrary-length message string, divide it in a 128 character blocks
        and represents each block with an integer. Return the lis of integers
        """

        return
    # Converts a string message to a list of block integers.

    def getTextFromBlocks(self, blockInts, blockSize):
        """
        Converts a list of block integers
        to the original message string.
        """

    def asciiconverter(self, a):
        """
        Takes input integer
        converts groups of 2 integers (hence text must be uppercase only) from ascii to text
        outputs string
        eg: a = 72697676798779827668 --> text output = 'HELLOWORLD'
        """
        pass

    def textconverter(self, s):
        """
        Takes input string
        converts characters of string into ascii representation
        eg: string input s = 'HELLOWORLD' -->  integer output = 72697676798779827668
        return integer
        """
        pass
