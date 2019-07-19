from itertools import permutations
try:	
	astr=input()
	arr=permutations(astr)
	for i in arr:
		print(''.join(i))
except ValueError:
	print("invalid")
	
