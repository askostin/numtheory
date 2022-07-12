# Test our functions

from numtheory.dividers import *

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
		gcd,
		[[0, 4], [4, 0], [6, 27], [15, 55], [33, 101], [100, 600]],
		[4, 4, 3, 5, 1, 100]
	)


def test_simplify_frac():
	general_test(
		simplify_frac,
		[(0, 4), (6, 27), (15, 55), (-8, 32), (100, 600), (-12, 18)],
		[(0, 1), (2, 9), (3, 11), (-1, 4), (1, 6), (-2, 3)]
	)


def test_float2frac():
	general_test(
		float2frac,
		[4, 1.25, 0, -8.3, 7.1, 2.04],
		[(4, 1), (5, 4), (0, 1), (-83, 10), (71, 10), (51, 25)]
	)


def test_divider_min():
	general_test(
		divider_min,
		[2, 5, 7, 15, 37, 49, 51],
		[2, 5, 7, 3, 37, 7, 3]
	)


def test_nondivisibles():
	general_test(
		nondivisibles,
		[[2, 10, [2, 3]], [12, 22, [3, 7]]],
		[[5, 7], [13, 16, 17, 19, 20, 22]]
	)


def test_first_divisible():
	general_test(
		first_divisible,
		[[2, 10, 3], [10, 20, 31], [15, 30, 15], [20, 40, 17]],
		[3, None, 15, 34]
	)


def test_sternbrocot_list():
	general_test(
		sternbrocot_list,
		[[0],
		 [1],
		 [2, 'Stern-Brocot', True],
		 [0, 'Farray'],
		 [1, 'Farray'],
		 [2, 'Farray', True]
		],
		[[(0, 1), (1, 0)],
		 [(0, 1), (1, 1), (1, 0)],
		 [(0, 1), (1, 2), (1, 1), (2, 1)],
		 [(0, 1), (1, 1)],
		 [(0, 1), (1, 2), (1, 1)],
		 [(0, 1), (1, 3), (1, 2), (2, 3), (1, 1)]
		]
	)


def test_encode_sternbrocot():
	general_test(
		encode_sternbrocot,
		[[2.71828, True, 8], [(27, 10)], [(19, 7)]],
		['RRLRRLRL', 'RRLRRLL', 'RRLRRL']
	)


def test_decode_sternbrocot():
	general_test(
		decode_sternbrocot,
		['LRRL', 'RRLRRLL', 'RRLRRL'],
		[(5, 7), (27, 10), (19, 7)]
	)


if __name__ == "__main__":
	print("\nTesting gcd():")
	test_gcd()

	print("\nTesting simplify_frac():")
	test_simplify_frac()

	print("\nTesting float2frac():")
	test_float2frac()

	print("\nTesting divider_min():")
	test_divider_min()

	print("\nTesting nondivisibles():")
	test_nondivisibles()

	print("\nTesting first_divisible():")
	test_first_divisible()

	print("\nTesting sternbrocot_list():")
	test_sternbrocot_list()

	print("\nTesting encode_sternbrocot():")
	test_encode_sternbrocot()

	print("\nTesting decode_sternbrocot():")
	test_decode_sternbrocot()
