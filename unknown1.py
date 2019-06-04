
try:
	num1=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	print(2*(arr[-1]+arr[-2]))
except ValueError:
	print("invalid")