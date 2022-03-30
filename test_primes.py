# Test our functions:

from . import primes, dividers

def test_primes():
	if (primes.primes_list(25) == primes.primes_list_by_sieve(25)):
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	if (primes.primes_list(200) == primes.primes_list_by_sieve(200)):
		print("Test 2 passed")
	else:
		print("Test 2 failed")

	if (primes.primes_list(800) == primes.primes_list_by_sieve(800)):
		print("Test 3 passed")
	else:
		print("Test 3 failed")

	if (primes.primes_list(4000) == primes.primes_list_by_sieve(4000)):
		print("Test 4 passed")
	else:
		print("Test 4 failed")

test_primes()
print("***************************************")

print(primes.primes_list_by_sieve(7))
print(dividers.nondivisibles_in_interval(2, 49, primes.primes_list_by_sieve(7)))

#print(primes.primes(4000))

print("***************************************")
print(primes.primes_list_by_sieve(200))
print(primes.primes_list_by_sieve(800))
print(primes.primes_list_by_sieve(4000))