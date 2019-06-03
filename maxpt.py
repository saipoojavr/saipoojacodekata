try:
	num=int(input())
	arr=list(map(int,input().split()))
	print(max(arr))
except ValueError:
	print("invalid")