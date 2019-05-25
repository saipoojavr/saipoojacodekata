try:
	num=int(input())
	a=0
	arr=[]
	pro=1
	while num>0:
	    a=num%10
	    arr.append(a)
	    num=num//10
	for i in range(0,len(arr)):
	    pro=pro*arr[i]
	print(pro)
except ValueError:
	print("invalid")