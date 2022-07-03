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
			primes_lst +=
				dvs.nondivisibles_in_interval(k*L + 1, (k + 1)*L, primes_lst)
		# process the interval [L*L + 1, n]
		if (L*L < n):
			primes_lst +=
				dvs.nondivisibles_in_interval(L*L + 1, n, primes_lst)
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

def prime_dividers(num: int):
	"""
	dividers : int -> listof(int)
	Returns sorted list of all prime dividers of the input number.
	"""
	# Elementary case
	if (num == 1):
		return []
	# Find the minimal divider @d of @num and unite it with recursively
	# founded dividers of @num/@d.
	else :
		d = dvs.divider_min(num)
		s = [d]
		return sorted([d] + prime_dividers(int(num/d)))


def prime_dividers2(num: int):
	"""
	dividers2 : N -> listof(list(N N))
	Returns the list of pairs [@d @p], where @d is a prime divider,
	and @p is the maximium power, where @d**@p is still a divider of @num.
	"""
	divs = prime_dividers(num)
	s = []
	for d in list(set(divs)):
		s = s + [[d, len(list(filter(lambda x: x == d, divs)))]]
	return sorted(s)


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
		prime_dividers = [pair[0] for pair in prime_dividers2(m)]
		n = 1
		d = 1
		for p in prime_dividers: # Fix code here
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
		all_dividers = prime_dividers2(m)
		dividers_powers = [pair[1] for pair in all_dividers]
		tmp = 1
		for pow in dividers_powers:
			tmp *= pow
		if tmp == 1:
			return (-1)**(len(all_dividers) % 2)
		else:
			return 0

