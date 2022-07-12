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
	flag = True
	for i, o, o_c in zip(input, output, output_cor):
		if (o != o_c):
			flag = False
			print("Fail: gcd({}) = {}, must be {}".format(i, o, o_c))
	if flag:
		print("Test passed")

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

if __name__ == "__main__":
	print("Testing gcd()")
	test_gcd()

	print("Testing simplify_frac()")
	test_simplify_frac()

	print("Testing float2frac()")
	test_float2frac()

	print("Testing divider_min()")
	test_divider_min()

	print("Testing nondivisibles()")
	test_nondivisibles()

	print("Testing first_divisible()")
	test_first_divisible()

	print("Testing sternbrocot_list()")
	test_sternbrocot_list()

	print("Testing encode_sternbrocot()")
	test_encode_sternbrocot()

	print("Testing decode_sternbrocot()")
	test_decode_sternbrocot()
