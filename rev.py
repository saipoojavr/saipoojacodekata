try:
	num=int(input())
	a=0
	arr=[]
	while num>0:
	    a=num%10
	    arr.append(a)
	    num=num//10
	for i in range(0,len(arr)):
	    print(arr[i],end="")
except ValueError:
	print("invalid")