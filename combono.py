try:
	num=int(input())
	arr=list(map(int,input().split()))
	print(num*(num+1)//2)
except ValueError:
	print("invalid")
