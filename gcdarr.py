from math import gcd
try:	
	num=int(input())
	arr =list(map(int,input().split()))  
	a = arr[0]
	for i in arr[1:]:
	  a =gcd(a, i)
	print(a)
except ValueError:
	print("invalid")