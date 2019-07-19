from itertools import permutations
astr=input()
arr=permutations(astr)
for i in arr:
	print(''.join(i))
	
