import math
from . import dividers as dvs


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
			primes_lst += \
				dvs.nondivisibles(k*L + 1, (k + 1)*L, primes_lst)
		# process the interval [L*L + 1, n]
		if (L*L < n):
			primes_lst += \
				dvs.nondivisibles(L*L + 1, n, primes_lst)
		return primes_lst


def primes_by_sieve(n: int):
	"""
	primes_list_by_sieve : N -> listof(N)
	For @n >=2 finds all prime numbers in the range [2, n] by the classical
	"Sieve of Eratosthenes" method.
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


def primes_quantity(n: int) -> int:
	"""
	Finds a quantity of prime numbers in the interval [2..@n].
	"""
	if (n < 2) or (not isinstance(n, int)):
		raise ValueError("Input should be integer not less than 2.")
	return len(primes(n))


def prime_dividers(n: int, pairs = False):
	""" dividers : int, bool -> listof(int) | listof( (N, N) )
	Returns sorted list of all prime dividers of the input number.

	1) If (@pairs == False) find the minimal divider @d of @n
	and unite it with recursively founded dividers of @n/@d.
	2) If (@pairs == True) returns the list of pairs [@d @p],
	where @d is a prime divider, and @p is the maximium power,
	where @d**@p is still a divider of @n.
	"""
	def aux(n):
		if (n == 1):
			return []
		else :
			d = dvs.divider_min(n)
			s = [d]
			return sorted([d] + aux(int(n/d)))
	if (n <= 1):
		return []
	all_divs = aux(n)
	if pairs:
		s = []
		for d in list(set(all_divs)):
			s = s + [[d, len(list(filter(lambda x: x == d, all_divs)))]]
		return sorted(s)
	else:
		return sorted(list(set(all_divs)))


def phi(m: int) -> int:
	"""
	Euler phi function phi(@m) returns quantity of whole numbers in the set
	{0, 1,... , m - 1}, which are mutually prime with @m.
	Examples:
	phi(1) = 1
	phi(p) = p - 1 (p is a prime number)
	phi(p^k) = p^{k} - p^{k-1}
	phi(m) = m * \prod_{p\m} (1 - 1/p)
	"""
	if m < 0:
		raise ValueError("Input should be positive integer.")
	elif (m == 1 or m == 2):
		return 1
	else:
		p_divs = [pair[0] for pair in prime_dividers(m, True)]
		n = 1
		d = 1
		for p in p_divs:
			n *= p-1
			d *= p
		return (n*m)//d


def mu(m: int) -> int:
	"""
	Möbius mu function mu(@m).
	"""
	if m < 0:
		raise ValueError("Input should be positive integer.")
	elif (m == 1):
		return 1
	else:
		all_dividers = prime_dividers(m, True)
		dividers_powers = [pair[1] for pair in all_dividers]
		tmp = 1
		for pow in dividers_powers:
			tmp *= pow
		if tmp == 1:
			return (-1)**(len(all_dividers) % 2)
		else:
			return 0

