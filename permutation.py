from itertools import permutations
n1=input()
arr=permutations(n1)
for i in arr:
	print(''.join(i))
	