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

def float_precision(num: float) -> int:
	"""
	Find number of digits on the right sight of the decimal point.
	"""
	if (num == math.trunc(num)):
		return 0
	else :
		string_form = str(num)
		num_parts = string_form.partition('.')
	return len(num_parts[2])

def float2frac(num: float) -> tuple:
	"""
	Converts decimal number to rational fraction in the form of tuple (n, d), where n and d are mutually prime.
	Analog of standard library function float.as_integer_ratio()
	"""
	if (num == math.trunc(num)):
		return (int(num), 1)
	else :
		sign = 1 if (num >= 0) else -1
		string_form = str(abs(num))
		num_parts = string_form.partition('.')
		whole = int(num_parts[0])
		frac = int(num_parts[2])
		frac_digits = len(num_parts[2])
		d = 10**frac_digits
		n = (d * whole + frac)
		gcd_nd = gcd(n, d)
		if (gcd_nd != 1) :
			n /= gcd_nd
			d /= gcd_nd
		return (int(sign*n), int(d))

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
				this_gcd = gcd(nom, den)
				nom = int(nom / this_gcd)
				den = int(den / this_gcd)
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

def encode_sternbrocot(number, limit_length = True, max_length = 20) :
	"""
	encode_sternbrocot : number, limit_length, max_length -> stringof(S)
	encode_sternbrocot : int/float/tuple, bool, int -> stringof(sym)
	where:
		- number can be:
			* integer number,
			* float number,
			* tuple (m, n), which represents the rational fraction m/n;
		- limit_length - whether we should constraint 
		- S = {'L', 'R'}.
	Write 'path' to a input fraction through the Stern-Brocot tree, where 'L' is for 'left', 'R' is for 'right'.
	"""
	def convert_pair(pair: tuple) :
		m = pair[0]
		n = pair[1]
		if (n == 0) :
			return 'RRR...'
		this_gcd = gcd(m, n)
		m = m / this_gcd
		n = n / this_gcd
		code = ''
		while (m != n) :
			if (m < n) :
				code += 'L'
				n = n - m
			else :
				code += 'R'
				m = m - n
		return code

	if ((type(number) is tuple and len(number) == 2) :
		return convert_pair(number)
	elif (type(number) is int) :
		return convert_pair((number, 1))
	elif ((type(number) is float) and (number == math.floor(number))) :
		return convert_pair((int(number), 1))
	elif (type(number) is float) :
		# 
		code = ''
		depth = 0
		if (number < 1) :
			code += 'L'
			number = number / (1 - number)
		elif (number > 1) :
			code += 'R'
			number = number / (number - 1)
		else :
			return code
		# нужно дать ограничение на точность
	else :
		print("Input number should not be negative, and have to be integer, float, or rational fraction represented by tuple (m, n), where m and n are non-negative integers.")

# Create function for maximal simplification of comparison by module based on eq. (4.37)-(4.40) from "Concrete Math"
