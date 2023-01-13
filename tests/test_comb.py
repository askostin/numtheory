# Test functions from comb.py module

from numtheory.tests.test import general_test
from numtheory.comb import *

def help():
	print("Test functions:\n")
	print("test_digits_permutations()")
	print("test_combinations()")

# code test from other package, need only as an example
def test_lms():
	general_test(
		lms,
		[[[1, 2, 3, 0, 1]],
		 [[3, 2, 2, 3, 4, 1, 1], True, False],
		 [[-1, 0, 1, 1, 0, 3, -2], False],
		 [[-1, 0, 1, 1, 0, -2, -1], False, False]],
		[[1, 2, 3],
		 [2, 2, 3, 4],
		 [1, 0],
		 [1, 1, 0, -2]]
	)
