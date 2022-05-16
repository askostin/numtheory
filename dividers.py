import math

def gcd(a, b: int) -> int:
        if ((a < 0) or (b < 0)) :
                raise ValueError('Both numbers have to be non-negative integers.')
        else :
	        return a if (b == 0) else gcd(b, a % b)

def dividers_all(num):
	"""
	dividers : int -> listof(int)

	Returns sorted list of all prime dividers of the input number.
	"""
	# Elementary case
	if (num == 1):
		return []
	# Find the minimal divider @d of @num and unite it with recursively founded dividers of @num/@d.
	else :
		d = divider_min(num)
		s = [d]
		return sorted([d] + dividers_all(num/d))


def divider_min(n):
	"""
	divider_min : int -> int/string

	Returns the smallest divider (>=1) of the input number (>1). If the number is prime, return an empty string ''.
	"""
	if ((n % 2) == 0):
		return 2
	else:
		d = 3
		while (d <= math.floor(n/3)):
			if ((n % d) == 0):
				return d
			else:
				d += 2
		return n


def dividers2(num):
	"""
	dividers2 : N -> listof(list(N N))

	Returns the list of pairs [@d @p], where @d is a prime divider, and @p is the maximium power, where @d**@p is still a divider of @num.
	"""
	dvs = dividers_all(num)
	s = []
	for d in list(set(dvs)):
		s = s + [[d, len(list(filter(lambda x: x == d, dvs)))]]
	return sorted(s)

def nondivisibles_in_interval(start:int, end:int, dividers):
	"""
	nondivisibles_in_interval(N N listof(N)) -> listof(N)

	Returns list of all numbers in the interval [@start, @end], where each number cannot be divided to any number from @dividers list.
	There is no repeats in @dividers, this list is sorted in the ascending order, all elements are integers >= 2.
	"""
	dividers = dividers or []
	if (start > end or dividers == []):
		print("Incorrect input values")
		return -1
	L = (end - start + 1)
	A = [True]*L
	for d in dividers:
		first_divisible = find_first_divisible(start, end, d)
		if first_divisible:
			A[first_divisible - start] = False
			for num in range(first_divisible + d, end + 1, d):
				A[num - start] = False
	d_list = []
	for i in range(0, L):
		if A[i]:
			d_list.append(start + i)
	return d_list


def find_first_divisible(start:int, end:int, div:int):
	"""
	find_first_divisible : N N N -> N or False

	Find the first number in the interval [@start, @end] which is divisible to @div.
	"""
	for n in range(start, end + 1):
		if n%div == 0:
			return n
	return False

def oddize(n:int):
	if ((0 <= n) and (n <= 9)):
		n = (n + 1) if (n%2 == 0) else n
		return n
	else:
		return -1

def evenize(n:int):
	if ((0 <= n) and (n <= 9)):
		n = n if (n%2 == 0) else n + 1
		return n
	else:
		return -1

# Create function for maximal simplification of comparison by module based on eq. (4.37)-(4.40) from "Concrete Math"
