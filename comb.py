# def factorial(n)

# For given number @n generate list of all various numbers,
# which are results of permutatiuons of digits of @n.
def permutations(n: int):
	s = str(n)
	perms = []
	def aux(lod: list, prefix = ""):
		if not lod:
			perms.append(prefix)
		for i in range(len(lod)):
			aux(lod[:i]+lod[i+1:], prefix + lod[i])

	aux(s)
	return list(set([int(x) for x in perms]))

# For given list of n various elements find number of combinations
# of k elements C_n^k.
def combinations
