# Test our functions

from .primes import *
from .dividers import *

def help():
	print("Test functions:")
	print("test_primes()")
	print("test_is_prime(n)")
	print("test_mu()")

help()

def test_primes():
	if (primes(25) == primes(25, 'sieve')):
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	if (primes(200) == primes(200, 'sieve')):
		print("Test 2 passed")
	else:
		print("Test 2 failed")

	if (primes(800) == primes(800, 'sieve')):
		print("Test 3 passed")
	else:
		print("Test 3 failed")

	if (primes(4000) == primes(4000, 'sieve')):
		print("Test 4 passed")
	else:
		print("Test 4 failed")

	print("***************************************")

	print(primes(7, 'sieve'))
	print(nondivisibles_in_interval(2, 49, primes(7, 'sieve')))

	#print(primes.primes(4000))

	print("***************************************")
	print(primes(200, 'sieve'))
	print(primes(800, 'sieve'))
	print(primes(4000, 'sieve'))


def test_is_prime(n: int):
	if n < 0:
		raise ValueError("Enter positive integer")
	lst = primes(n)
	primes_len = len(lst)

	counter = 0
	for i in lst:
		if is_prime(i):
			counter += 1
	if counter == primes_len:
		print("is_prime() function works correctly.")
		print(lst)
	else :
		print("is_prime() function has bugs.")

def test_mu():
	if mu(1) == 1:
		print("Passed: mu(1) == 1")
	if mu(2) == -1:
		print("Passed: mu(2) == -1")
	if mu(3) == -1:
		print("Passed: mu(3) == -1")
	if mu(4) == 0:
		print("Passed: mu(4) == 0")
	if mu(5) == -1:
		print("Passed: mu(5) == -1")
	if mu(6) == 1:
		print("Passed: mu(6) == 1")
	if mu(7) == -1:
		print("Passed: mu(7) == -1")
	if mu(8) == 0:
		print("Passed: mu(8) == 0")
	if mu(9) == 0:
		print("Passed: mu(9) == 0")
	if mu(10) == 1:
		print("Passed: mu(10) == 1")
	if mu(11) == -1:
		print("Passed: mu(11) == -1")
	if mu(12) == 0:
		print("Passed: mu(12) == 0")
