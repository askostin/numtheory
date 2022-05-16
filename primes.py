import math
from . import dividers

def is_prime(n: int) :
        """
        Check if the number is a prime.
        """
        pass        

def primes_quantity(n: int) :
	"""
	primes_q : N -> N
	Finds a quantity of prime numbers in the interval [1..@n].
	"""
	if (n >= 1) and (n <= 3):
		return n - 1
	else :
		if (n % 2 == 0):
			return primes_quantity(n - 1)
		else :
			q = 0
			for i in range(5, n + 1, 2):
				if (n == dividers.divider_min(n)):
					q += 1

def primes_list(n: int):
	"""
	primes : N -> listof(N)
	For natural @n >= 1 returns all primes in the interval [1, n].
	"""
	if (n <= 1):
		return -1
	elif (n <= 1000):
		return primes_list_by_sieve(n)
	else :
		L = math.floor(math.sqrt(n))
		# Create list of primes up to the maximal value, which can be divider in the two-part multiplication @max_prime*@max_prime <= n
		primes_lst = primes_list_by_sieve(L)
		# print(primes_list) ### DELETE
		# Process the intervals [k*L + 1, k*L + L], k = 1..L-1
		for k in range (1, L):
			primes_lst += dividers.nondivisibles_in_interval(k*L + 1, (k + 1)*L, primes_lst)
			# print(nondivisibles_in_interval(k*L + 1, (k + 1)*L, primes_list)) ### DELETE
		# process the interval [L*L + 1, n]
		if (L*L < n):
			primes_lst += dividers.nondivisibles_in_interval(L*L + 1, n, primes_lst)
			# print(nondivisibles_in_interval(L*L + 1, n, primes_list)) ### DELETE
		return primes_lst

def primes_list_by_sieve(n: int):
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

#def primes(n) :
	"""
	primes : N -> listof(N)
	primes(n) creates list of all prime numbers in the interval [1..n], n > 1.
	"""
	# ...

#def build_SternBrocot_list(level: int, drop_inf = False): 
	"""
	build_SternBrocot_list : N, bool -> listof((N, N))
	build_SternBrocot_list(level, drop_inf) creates list of fractions, based on Stern-Brocot tree:
		- level (int) -
		- drop_inf (bool, default = False) - should we remove the tuple (1, 0), i.e. fraction 1/0 = infinity, from the output list.
	Representation:
		Fraction m/n is represented by tuple (m, n).
	Examples:
		- list for level 0 tree: [(0, 1), (1, 0)]
		- list for level 1 tree: [(0, 1), (1, 1), (1, 0)]
		- list for level 2 tree: [(0, 1), (1, 2), (1, 1), (2, 1), (1, 0)]l
	Algorithm:
		Between each two adjacent tuples (m, n) and (m', n') we place the new tuple (m + m', n + n').
	"""

#    lst = [(0, 1), (1, 0)]
#    if level < 0 :
#        return ("Level should be >= 0")
#    else :
#        ...
