# Test functions from dividers.py module

from numtheory.primes import *
from numtheory.dividers import *

def help():
	print("Test functions:\n")
	print("test_is_prime()")
	print("test_prime_dividers()")
	print("test_primes()")
	print("test_primes_quantity()")
	print("test_phi()")
	print("test_mu()")

def test_is_prime():
	lst_corr = primes(3000)
	lst_incorr = [x**2 for x in range(4,36)]
	primes_len = len(lst_corr)
	nonprimes_len = len(lst_incorr)
	c1 = 0
	c2 = 0
	primes_with_problems = []
	nonprimes_with_problems = []
	for x in lst_corr:
		if is_prime(x):
			c1 += 1
		else:
			primes_with_problems.append(x)
	for x in lst_incorr:
		if (not is_prime(x)):
			c2 += 1
		else:
			nonprimes_with_problems.append(x)
	if (c1 == primes_len) and (c2 == nonprimes_len):
		print("is_prime() function works correctly.")
	else :
		print("is_prime() has bugs:")
		if (c1 != primes_len):
			print("counted {} as primes from {} primes".format(c1, primes_len))
			print(primes_with_problems)
		if (c2 != nonprimes_len):
			print("counted {} as non-primes from {} non-primes".\
				format(c2, nonprimes_len))
		print(nonprimes_with_problems)


def test_prime_dividers():
	input = [1, 12, 55, 100, 2047, 11011, 11111]
	output1_corr = [ \
		[], \
		[2, 3], \
		[5, 11], \
		[2, 5], \
		[23, 89], \
		[7, 11, 13], \
		[41, 271]]
	output2_corr = [ \
		[], \
		[[2, 2], [3, 1]], \
		[[5, 1], [11, 1]], \
		[[2, 2], [5, 2]], \
		[[23, 1], [89, 1]], \
		[[7, 1], [11, 2], [13, 1]], \
		[[41, 1], [271, 1]]]
	output1 = [prime_dividers(x, False) for x in input]
	output2 = [prime_dividers(x, True) for x in input]
	if (output1 == output1_corr) and (output2 == output2_corr):
		print("prime_dividers() works correctly")
	else:
		print("prime_dividers() doesn't work correctly:")
		print("the output(s) from ", input)
	if (output1 != output1_corr):
		print("in short form is")
		print(output1)
	if (output2 != output2_corr):
		print("in full paired form is")
		print(output2)


def test_primes():
	if (primes(25) == primes(25, 'sieve')):
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	if (primes(200) == primes(200, 'sieve')):
		print("Test 2 passed")
	else:
		print("Test 2 failed")

	if (primes(800) == primes(800, 'sieve')):
		print("Test 3 passed")
	else:
		print("Test 3 failed")

	if (primes(4000) == primes(4000, 'sieve')):
		print("Test 4 passed")
	else:
		print("Test 4 failed")

	print("***************************************")
	print("Prime numbers in the range [1, 2000]:")
	print(primes(2000))


def test_primes_quantity():
	input = [2, 3, 5, 11, 55, 100]
	output_correct = [1, 2, 3, 5, 16, 25]
	output = [primes_quantity(x) for x in input]
	if (output == output_correct):
		print("primes_quantity() works correctly")
	else:
		print("primes_quantity() works incorrectly:")
		print("the output from ", input, " is ", output)


def test_phi():
	input = \
		[1] + \
		[7, 47, 83, 103, 701, 1289, 2557, 3571] + \
		[2**2, 5**2, 11**2, 41**2] + \
		[12, 18, 36]
	output_correct = \
		[1] + \
		[6, 46, 82, 102, 700, 1288, 2556, 3570] + \
		[2, 20, 11**2-11, 41**2-41] + \
		[4, 6, 12]
	output = [phi(x) for x in input]
	if (output == output_correct):
		print("phi() works correctly")
	else:
		print("phi works incorrectly:")
		for i, o, o_c in zip(input, output, output_correct):
			if o != o_c:
				print("phi({}) = {}, have to be {}".format(i, o, o_c))


def test_mu():
	if mu(1) == 1:
		print("Passed: mu(1) == 1")
	if mu(2) == -1:
		print("Passed: mu(2) == -1")
	if mu(3) == -1:
		print("Passed: mu(3) == -1")
	if mu(4) == 0:
		print("Passed: mu(4) == 0")
	if mu(5) == -1:
		print("Passed: mu(5) == -1")
	if mu(6) == 1:
		print("Passed: mu(6) == 1")
	if mu(7) == -1:
		print("Passed: mu(7) == -1")
	if mu(8) == 0:
		print("Passed: mu(8) == 0")
	if mu(9) == 0:
		print("Passed: mu(9) == 0")
	if mu(10) == 1:
		print("Passed: mu(10) == 1")
	if mu(11) == -1:
		print("Passed: mu(11) == -1")
	if mu(12) == 0:
		print("Passed: mu(12) == 0")


if __name__ == '__main__':
	print("\nTesting test_is_prime():")
	test_is_prime()
	print("\nTesting test_prime_dividers():")
	test_prime_dividers()
	print("\nTesting test_primes():")
	test_primes()
	print("\nTesting test_primes_quantity():")
	test_primes_quantity()
	print("\nTesting test_phi():")
	test_phi()
	print("\nTesting test_mu():")
	test_mu()
