# Test our functions

from . import primes, dividers

def test_primes():
	if (primes.primes(25) == primes.primes(25, 'sieve')):
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	if (primes.primes(200) == primes.primes(200, 'sieve')):
		print("Test 2 passed")
	else:
		print("Test 2 failed")

	if (primes.primes(800) == primes.primes(800, 'sieve')):
		print("Test 3 passed")
	else:
		print("Test 3 failed")

	if (primes.primes(4000) == primes.primes(4000, 'sieve')):
		print("Test 4 passed")
	else:
		print("Test 4 failed")

	print("***************************************")

	print(primes.primes(7, 'sieve'))
	print(dividers.nondivisibles_in_interval(2, 49, primes.primes(7, 'sieve')))

	#print(primes.primes(4000))

	print("***************************************")
	print(primes.primes(200, 'sieve'))
	print(primes.primes(800, 'sieve'))
	print(primes.primes(4000, 'sieve'))


def test_is_prime(n: int):
	if n < 0:
		raise ValueError("Enter positive integer")
	lst = primes.primes(n)
	primes_len = len(lst)
	
	counter = 0
	for i in lst:
		if primes.is_prime(i):
			counter += 1
	if counter == primes_len:
		print("is_prime() function works correctly.")
		print(lst)
	else :
		print("is_prime() function has bugs.")

if __name__ == '__main__':
	test_primes()
	test_is_prime(1000)
