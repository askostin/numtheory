from . import dividers, primes
import math

def factorial_stirling(n: int) :
	if (n < 0) :
		raise ValueError('Error, input should be non-negative integer')
	else :
		return round(math.sqrt(2 * math.pi * n) * pow((n / math.e), n))

def oddize(n: int):
	if ((0 <= n) and (n <= 9)):
		n = (n + 1) if (n%2 == 0) else n
		return n
	else:
		return -1

def evenize(n: int):
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

