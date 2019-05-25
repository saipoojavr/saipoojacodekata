try:
	num1=int(input())
	a=0
	arr=[]
	while num1>0:
	    a=num1%10
	    arr.append(a)
	    num1=num1//10
	for i in range(0,len(arr)):
	    print(arr[i],end="")
except ValueError:
	print("invalid")
