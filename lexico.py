try:
	num=int(input())
	a=[]
	for i in range(0,num):
		arr=input()
		a.append(arr)
	b=sorted(a)
	print(*b)
except ValueError:
	print("invalid")