try:
	num=int(input())
	a=0
	arr=[]
	while num>0:
	    a=num%10
	    arr.append(a)
	    num=num//10
	    arr.sort()
	for i in range(-1,-len(arr)-1,-1):
	    print(arr[i],end="")
except ValueError:
	print("invalid")
