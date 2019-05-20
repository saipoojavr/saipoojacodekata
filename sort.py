try:
	arr=int(input())
	list=[int(i) for i in input().split()]
	list.sort()
	print(*list,sep=" ")
except ValueError:
	print("invalid")