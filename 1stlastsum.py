try:
	num=int(input())
	a=0
	arr=[]
	while num>0:
	    a=num%10
	    arr.append(a)
	    num=num//10
	print(arr[0]+arr[-1])
except ValueError:
	print("invalid")