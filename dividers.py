import math


def gcd(a, b: int) -> int:
	if ((a < 0) or (b < 0)):
		raise ValueError('Both numbers have to be non-negative integers.')
	else:
		return a if (b == 0) else gcd(b, a % b)


def simplify_frac(pair: tuple) -> tuple:
	"""For pair (a, b) of two integers (b > 0), which represents fraction a/b,
	return simplified fraction, where nominator and denominator are divided
	to their GCD.
	"""
	n = pair[0]
	d = pair[1]
	if ((type(n) != int) or (type(d) != int) or (d < 0)):
		raise ValueError('Both numbers in pair have to be integers,\
			the second should be positive.')
	elif (d == 0):
		return (1, 0)
	else:
		gcd_nd = gcd(abs(n), d)
		if (gcd_nd != 1):
			n = n / gcd_nd
			d = d / gcd_nd
		return (int(n), int(d))


def float2frac(num: float) -> tuple:
	"""Converts decimal number to rational fraction in the form of tuple
	(n, d), where n and d are mutually prime. Analog of standard library
	function float.as_integer_ratio()
	"""
	if (num == math.trunc(num)):
		return (int(num), 1)
	sign = 1 if (num >= 0) else -1
	string_form = str(abs(num))
	num_parts = string_form.partition('.')
	whole = int(num_parts[0])
	frac = int(num_parts[2])
	frac_digits = len(num_parts[2])
	d = 10**frac_digits
	n = sign*(d * whole + frac)
	return simplify_frac((n, d))


def divider_min(n: int) -> int:
	"""Returns the smallest divider (> 1) of the input number (>1).
	"""
	if ((n < 2) or (not isinstance(n, int))):
		raise ValueError('Input number has to be integer > 1.')
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


def nondivisibles(start: int, end: int, dividers):
	"""Returns list of all numbers in the interval [@start, @end],
	where each number cannot be divided to any number from @dividers list.
	There is no repeats in @dividers, this list is sorted in the ascending
	order, all elements are integers >= 2.
	"""
	dividers = dividers or []
	if (start > end or dividers == []):
		print("Incorrect input values")
		return -1
	L = (end - start + 1)
	A = [True]*L
	for d in dividers:
		first_div = first_divisible(start, end, d)
		if first_div:
			A[first_div - start] = False
			for num in range(first_div + d, end + 1, d):
				A[num - start] = False
	d_list = []
	for i in range(0, L):
		if A[i]:
			d_list.append(start + i)
	return d_list


def first_divisible(start: int, end: int, div: int):
	"""Finds the first number in the interval [@start, @end]
	which is divisible to @div.
	"""
	for n in range(start, end + 1):
		if n%div == 0:
			return n
	return None


def sternbrocot_list(
		level: int,
		/,
		seq_type = 'Stern-Brocot',
		drop_inf = False
	):
	"""sternbrocot_list : N, str, bool -> listof((N, N))
	sternbrocot_list(level, drop_inf) creates list of fractions,
	based on Stern-Brocot tree (in the interval [0, +inf]) or
	Farray sequence (in the interval [0, 1]):
		- level (int) - depth of the tree, number of iterations
		  when we insert new fractions;
		- seq_type (str) - 'Stern-Brocot' (default) or
		  'Farray' sequence (list) to build;
		- drop_inf (bool, default = False) - should we
		  remove the tuple (1, 0)  (by definition, fraction 1/0 = +infinity)
		  from Stern-Brocot output sequence.
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
		Between each two adjacent tuples (m, n) and (m', n')
	we place the new tuple (m + m', n + n').
	"""

	def insert_tuples(lst: list, n: int):
		if (n == 0):
			return lst
		else :
			iterations = len(lst) - 1
			new_tuples = []
			for i in range(iterations):
				nom = lst[i][0] + lst[i+1][0]
				den = lst[i][1] + lst[i+1][1]
				new_tuples.append( simplify_frac((nom, den)) )
			new_lst = []
			for i in range(iterations):
				new_lst = new_lst + [lst[i], new_tuples[i]]
			new_lst.append(lst[-1])
			return insert_tuples(new_lst, n-1)

	if level < 0:
		return ("Level should be >= 0")
	if (seq_type == 'Farray'):
		lst = [(0, 1), (1, 1)]
		result = insert_tuples(lst, level)
	else:
		lst = [(0, 1), (1, 0)]
		result = insert_tuples(lst, level)
		result = result[:-1] if drop_inf else result
	return result


def encode_sternbrocot(number, limit_length = True, max_length = 20):
	"""encode_sternbrocot : number, limit_length, max_length -> stringof(S)
	where:
		- number can be:
			* integer number,
			* float number,
			* tuple (m, n), which represents the rational fraction m/n;
		- limit_length - whether we should constraint,
		- S = {'L', 'R'}.
	Write 'path' to a input fraction through the Stern-Brocot tree,
	where 'L' is for 'left', 'R' is for 'right'.
	"""
	def convert_pair(pair: tuple):
		m = pair[0]
		n = pair[1]
		if (n == 0):
			return 'RRR...'
		m, n = simplify_frac(pair)
		code = ''
		i = 0
		while (m != n):
			if (m < n):
				code += 'L'
				n = n - m
			else :
				code += 'R'
				m = m - n
			i += 1
			if (limit_length and i >= max_length):
				return code
		return code

	if ((type(number) is tuple) and (len(number) == 2)):
		return convert_pair(number)
	elif (type(number) is int):
		return convert_pair((number, 1))
	elif ((type(number) is float) and (number == math.floor(number))) :
		return convert_pair((int(number), 1))
	elif (type(number) is float):
		return convert_pair(float2frac(number))
	else:
		print("Input number should not be negative, and have to be integer, \
			float, or rational fraction represented by tuple (m, n), \
			where m and n are non-negative integers.")


def decode_sternbrocot(code: str) -> float:
	"""Convert code for number in Stern-Brocot tree in the form 'LRRLRLLL...'
	back to the number itself.
	"""
	left_number = (0, 1)
	curr_number = (1, 1)
	right_number = (1, 0)

	for s in code:
		if (s.upper() == 'R'):
			adj_number = right_number
			left_number = curr_number
		elif (s.upper() == 'L'):
			adj_number = left_number
			right_number = curr_number
		else:
			raise ValueError("Wrong code! \
				Only 'L' and 'R' symbols are allowed.")

		curr_number = \
			simplify_frac(
				(curr_number[0] + adj_number[0],
				 curr_number[1] + adj_number[1])
			)

	return curr_number
