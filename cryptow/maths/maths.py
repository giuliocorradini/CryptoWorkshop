import logging

def gcd(a, b):
    '''
    Computes the greatest common divisor using Euclid's extended
    algorithm.
    :param a: positive integer
    :param b: positive integer <= a
    :return: positive integer
    '''

    if b == 0:
        return a

    if b > a:
        return gcd(b, a)

    seq = [a, b, a%b]
    while seq[2] != 0:
        logging.debug(f"GCD compute step: {seq}")
        seq.pop(0)
        seq.append(seq[0] % seq[1])

    return seq[1]



def phi(n):
    '''
    Computes Euler's phi function. First rough implementation.
    :param n: Positive integer to compute the totient of
    :return: The number of coprimes of n in range [1, N)
    '''

    # 1 is always coprime with every number, therefore is skipped
    coprimes = 1

    for i in range(2, n):
        if gcd(i, n) == 1:  # coprimes only share 1 as common divisor
            coprimes += 1

    return coprimes
