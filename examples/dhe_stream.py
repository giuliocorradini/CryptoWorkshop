from cryptow.keygen import DiffieHellmanActor
from io import BufferedIOBase
import logging
import argparse
import sys
import socket

'''
Implementation of Diffie & Hellman key exchange using streams for IPC.
The class DHExchangeStream connects to a stream that may represent a
TCP socket or a UNIX domain socket.
'''

class DHExchangeStream:
    def __init__(self, rstream: BufferedIOBase, wstream: BufferedIOBase):
        self.rstream = rstream
        self.wstream = wstream

        self.actor = DiffieHellmanActor()

    def alice_behaviour(self):
        x = self.actor.generate_public()
        self.wstream.write(f"{self.actor.n},{self.actor.r},{x}\n")
        self.wstream.flush()

        try:
            y = int(self.rstream.readline())
        except ValueError:
            logging.error("Can't parse public key part from Bob")
            return

        shared = self.actor.complete_key(y)
        return shared

    def bob_behaviour(self):
        n, r, x = list(
            map(int, self.rstream.readline().split(','))
        )
        self.actor.n, self.actor.r = n, r

        y = self.actor.generate_public()
        self.wstream.write(f"{y}\n")
        self.wstream.flush()

        shared = self.actor.complete_key(x)
        return shared


def main(role, host, port):
    #   Open socket with peer
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if role == 'Bob':  # listen
            s.bind((host, port))
            s.listen(1)
            cs, cl_addr = s.accept()
            rfile = open(cs.fileno(), 'r')
            wfile = open(cs.fileno(), 'w')
        else:
            s.connect((host, port))
            rfile = open(s.fileno(), 'r')
            wfile = open(s.fileno(), 'w')

        #   Pass socket r/w streams to protocol
        dhe = DHExchangeStream(rfile, wfile)

        #   Act as either Alice or Bob
        if role == 'Alice':
            print(dhe.alice_behaviour())
        else:
            print(dhe.bob_behaviour())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=9999)
    parser.add_argument('--role', choices=['Alice', 'Bob'], default='Alice')

    args = parser.parse_args(sys.argv[1:])

    main(args.role, args.host, args.port)