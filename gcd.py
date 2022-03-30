import math

def gcd(a, b):
	"""
    gcd : N N -> N
	gcd(a,b) finds the greatest common divider of the two whole numbers @a and @b, where both of them are != 0.
	The function is implemented using Euclid algorithm.
	"""
	a_abs = abs(a)
	b_abs = abs(b)
	if (a_abs == b_abs):
		return a_abs
	else :
		n_min = min(a_abs, b_abs)
		n_max = max(a_abs, b_abs)
		return gcd_eucl(n_min, n_max)

def gcd_eucl(n1, n2):
	"""
	gcd_eucl : N N -> N
	gcd_eucl(n1, n2) is a reccurrent Euclidian algorithm to find @gcd, 0 <= n1 < n2.
	"""
	if (n1 == 0):
		return n2
	else :
		return gcd_eucl(n2 % n1, n1)
