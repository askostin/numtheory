import math
from . import dividers

def is_prime(n: int) :
	"""
	Check if the number is a prime.
	"""
	if n < 2 :
		raise ValueError("Input should be integer not less than 2.")
	elif [2, 3].count(n) :
		return True
	elif (n % 2 == 0) :
		return False
	else :
		for i in range (5, n, 2) :
			if (n % i == 0) :
				return False
		return True

def primes_quantity(n: int) :
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

def SternBrocot_list(level: int, seq_type = 'Stern-Brocot', drop_inf = False):
	"""
	SternBrocot_list : N, str, bool -> listof((N, N))
	SternBrocot_list(level, drop_inf) creates list of fractions, based on Stern-Brocot tree (in the interval [0, +inf]) or Farray sequence (in the interval [0, 1]):
		- level (int) - depth of the tree, number of iterations when we insert new fractions;
		- seq_type (str) - 'Stern-Brocot' (default) or 'Farray' sequence (list) to build;
		- drop_inf (bool, default = False) - should we remove the tuple (1, 0)  (by definition, fraction 1/0 = +infinity) from Stern-Brocot output sequence.
	Representation:
		Fraction m/n is represented by tuple (m, n).
	Examples:
	1. For SternBrocot tree:
		- list for level 0 tree: [(0, 1), (1, 0)]
		- list for level 1 tree: [(0, 1), (1, 1), (1, 0)]
		- list for level 2 tree: [(0, 1), (1, 2), (1, 1), (2, 1), (1, 0)]
	2. For Farray sequence:
		- list for level 0 tree: [(0, 1), (1, 1)]
		- list for level 1 tree: [(0, 1), (1, 2), (1, 1)]
		- list for level 2 tree: [(0, 1), (1, 3), (1, 1), (2, 3), (1, 1)]
	Algorithm:
		Between each two adjacent tuples (m, n) and (m', n') we place the new tuple (m + m', n + n').
	"""

	def insert_tuples(lst: list, n: int) :
		if (n == 0) :
			return lst
		else :
			iterations = len(lst) - 1
			new_tuples = []
			for i in range(iterations) :
				nom = lst[i][0] + lst[i+1][0]
				den = lst[i][1] + lst[i+1][1]
				gcd = dividers.gcd(nom, den)
				nom = int(nom / gcd)
				den = int(den / gcd)
				new_tuples.append( (nom, den) )
			new_lst = []
			for i in range(iterations) :
				new_lst = new_lst + [lst[i], new_tuples[i]]
			new_lst.append(lst[-1])
			return insert_tuples(new_lst, n-1)

	if level < 0 :
		return ("Level should be >= 0")
	else :
		if (seq_type == 'Farray') :
			lst = [(0, 1), (1, 1)]
			result = insert_tuples(lst, level)
		elif (seq_type == 'Stern-Brocot') :
			lst = [(0, 1), (1, 0)]
			result = insert_tuples(lst, level)
			result = result[:-1] if drop_inf else result
		return result
