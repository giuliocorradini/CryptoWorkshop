# CryptoWorkshop
Implementation of cryptographic functions in Python.
All the materials were sourced from "Systems and Networks"
course in my school.

## Tools
Subject-wide functions and other common facilities.

### Euler's totient function
*a.k.a. phi function*

> The phi function of a given integer *n* counts the positive
> integers up to *n* that a coprime with *n*.

Two coprime numbers only share 1 as a common factor.


Let's give an example: 𝜑(4) = ... 

4 is factored as 1 x 2 x 2; the numbers from 1 to 4 (n)
that are coprime with 4 (n) are 1 and 3.

[**1**, 2, **3**, 4], hence 𝜑(4) = 2

#### Properties
1. *n* is prime => 𝜑(n) = n - 1
2. a, b are coprimes => 𝜑(a*b) = 𝜑(a)*𝜑(b)
3. N = p1 * p2 with p1, p2 primes => 𝜑(N) = 𝜑(p1)*𝜑(p2)
= (p1-1)(p2-1)
    - Note that prime numbers are also coprimes with every other number.
4. 
5. 

#### Implementation
We offer a routine to compute Euler's totient for a given number.

The code is under `maths/totient.py`