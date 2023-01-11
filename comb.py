# def factorial(n)

# For given number @n generate list of all various numbers,
# which are results of permutatiuons of digits of @n.
def digits_permutations(n: int):
	s = str(n)
	perms = []
	def aux(lod: list, prefix = ""):
		if not lod:
			perms.append(prefix)
		for i in range(len(lod)):
			aux(lod[:i]+lod[i+1:], prefix+lod[i])

	aux(s)
	return list(set([int(x) for x in perms]))

# For given list of numbers build list of all combinations
# of @k elements from this list.
def combinations(lon: list, k: int):
	combs = []

	def aux(lon: list, k: int, prefix = []):
		if k == 0:
			tmp = sorted(prefix)
			if tmp not in combs:
				combs.append(tmp)
		for i in range(len(lon)):
			aux(lon[:i]+lon[i+1:], k-1, prefix+[lon[i]])

	aux(lon, k)
	return(combs)
