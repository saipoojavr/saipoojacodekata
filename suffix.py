try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(1):
		for j in range(i,num):
			a.append(str(sum(arr[:j+1])))
	a=a[::-1]
	print(" ".join(a))
except ValueError:
	print("invalid")