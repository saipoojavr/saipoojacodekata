try:
	num=map(int,input().split())
	l=[int(x) for x in input().split()]
	arr=[]
	for i in range(0,len(l)-1):
		for j in range(i+1,len(l)):
			if l[i]-l[j]!=0:
				arr.append(abs(l[i]-l[j]))
	print(min(arr))
except ValueError:
	print("invalid")	