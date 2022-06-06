import math
from . import dividers

def is_prime(n: int):
	"""
	Check if the number is a prime.
	"""
	if n < 2:
		raise ValueError("Input should be integer not less than 2.")
	elif [2, 3].count(n):
		return True
	elif (n % 2 == 0):
		return False
	else :
		for i in range (5, n, 2):
			if (n % i == 0):
				return False
		return True

def primes_quantity(n: int):
	"""
	primes_q : N -> N
	Finds a quantity of prime numbers in the interval [2..@n].
	"""
	if [2, 3].count(n):
		return n - 1
	else :
		if (n % 2 == 0):
			return primes_quantity(n - 1)
		else :
			q = 0
			for i in range(5, n + 1, 2):
				if (n == dividers.divider_min(n)):
					q += 1

def primes(n: int, method = 'general'):
	"""
	primes : N -> listof(N)
	For natural @n >= 1 returns all primes in the interval [2, n].
	"""
	if (n <= 1):
		return -1
	elif (n <= 1000) or (method == 'sieve'):
		return primes_by_sieve(n)
	else :
		L = math.floor(math.sqrt(n))
		# Create list of primes up to the maximal value, which can be divider
		# in the two-part multiplication @max_prime*@max_prime <= n.
		primes_lst = primes_by_sieve(L)
		# Process the intervals [k*L + 1, k*L + L], k = 1..L-1
		for k in range (1, L):
			primes_lst += dividers.nondivisibles_in_interval(k*L + 1, (k + 1)*L, primes_lst)
		# process the interval [L*L + 1, n]
		if (L*L < n):
			primes_lst += dividers.nondivisibles_in_interval(L*L + 1, n, primes_lst)
		return primes_lst

def primes_by_sieve(n: int):
	"""
	primes_list_by_sieve : N -> listof(N)
	For @n >=2 finds all prime numbers in the range [2, n] by the classical "Sieve of Eratosthenes" method.
	"""
	if (n <= 1):
		return -1
	elif (n == 2):
		return [2]
	else:
		A = (n + 1) * [True]
		A[0] = A[1] = False
		for k in range(2, n + 1):
			if A[k]:
				for p in range(k*k, n + 1, k):
					A[p] = False
		primes_lst = []
		for k in range(2, n + 1):
			if A[k]:
				primes_lst.append(k)
		return(primes_lst)