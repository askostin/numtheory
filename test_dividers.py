# Test our functions

import numtheory.dividers as d

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


def general_test(fun, input, output_cor):
	if (len(input) != len(output_cor)):
		raise ValueError('Input and ouput are to have the same size.')
	if (isinstance(input[0], list)):
		output = [fun(*val) for val in input]
	else:
		output = [fun(val) for val in input]
	flag = True
	print("\nTesting {}():".format(fun.__name__))
	for i, o, o_c in zip(input, output, output_cor):
		if (o != o_c):
			flag = False
			print(
				"Fail: {}({}) = {}, must be {}"\
				.format(fun.__name__,i, o, o_c)
			)
	if flag:
		print("Test passed")


def test_gcd():
	general_test(
		d.gcd,
		[[0, 4], [4, 0], [6, 27], [15, 55], [33, 101], [100, 600]],
		[4, 4, 3, 5, 1, 100]
	)


def test_simplify_frac():
	general_test(
		d.simplify_frac,
		[(0, 4), (6, 27), (15, 55), (-8, 32), (100, 600), (-12, 18)],
		[(0, 1), (2, 9), (3, 11), (-1, 4), (1, 6), (-2, 3)]
	)


def test_float2frac():
	general_test(
		d.float2frac,
		[4, 1.25, 0, -8.3, 7.1, 2.04],
		[(4, 1), (5, 4), (0, 1), (-83, 10), (71, 10), (51, 25)]
	)


def test_divider_min():
	general_test(
		d.divider_min,
		[2, 5, 7, 15, 37, 49, 51],
		[2, 5, 7, 3, 37, 7, 17]
	)


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
