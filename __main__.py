from . import dividers, primes
import math

def factorial_stirling(n: int) :
    if (n < 0) :
        raise ValueError('Error, input should be non-negative integer')
    else :
        return round(math.sqrt(2 * math.pi * n) * pow((n / math.e), n))
