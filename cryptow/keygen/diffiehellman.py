import random

class DiffieHellmanActor:
    def __init__(self, actor = None):
        if actor:
            self.n = actor.n
            self.r = actor.r

        else:
            self.n = random.getrandbits(64)
            self.r = random.getrandbits(64)

        self.private = 0

    def generate_public(self):
        self.private = random.getrandbits(64)    #either a or b

        #   Don't do r**private%n as it's orders of magnitude slower.
        #   The pow function performs modulus every exponentiation step.
        self.public = pow(self.r, self.private, self.n)

        return self.public

    def complete_key(self, public):
        if self.private != 0:
            self.shared = pow(public, self.private, self.n)
        else:
            raise ValueError("Private key has not been generated yet.")

        return self.shared
