from cryptow.keygen import DiffieHellmanActor

def main():
    #   Instantiation of DiffieHellmanActor with no arg generates n and r
    #   Alice opens the connection and generates n, r
    alice = DiffieHellmanActor()

    #   Istantiation from a DiffieHellmanActor copies n and r
    bob = DiffieHellmanActor(alice)

    #   Let's generate public keys (X: Alice; Y: Bob)
    x = alice.generate_public()
    y = bob.generate_public()

    #   Share public keys and come to a shared secret
    shared_a = alice.complete_key(y)
    shared_b = bob.complete_key(x)

    print(f"Alice result: {shared_a}")
    print(f"Bob result: {shared_b}")

if __name__ == '__main__':
    main()
