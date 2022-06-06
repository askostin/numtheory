from .primes import mu

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
