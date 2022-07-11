# Test our functions

from .primes import *
from .dividers import *

def help():
	print("test_gcd()")
	print("test_simplify_frac()")
	print("test_float2frac()")
	print("test_divider_min()")
	print("test_nondivisibles()")
	print("test_first_divisible()")
	print("test_sternbrocot_list()")
	print("test_encode_sternbrocot()")
	print("test_decode_sternbrocot()")


def test_gcd():
	input = [(0, 4), (4, 0), (6, 27), (15, 55), (33, 101), (100, 600)]
	output_cor = [4, 4, 3, 5, 1, 100]
	output = [gcd(tp) for tp in input]
	for o, o_c in zip(output, output_cor):
		...

def test_simplify_frac():
	pass


def test_float2frac():
	pass


def test_divider_min():
	pass


def nondivisibles():
	pass


def first_divisible():
	pass


def sternbrocot_list():
	pass


def encode_sternbrocot():
	pass


def decode_sternbrocot():
	pass
