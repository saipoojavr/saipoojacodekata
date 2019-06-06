try:
	num=int(input())
	a=0
	sum=0
	arr=[]
	while num>0:
	    a=num%10
	    arr.append(a)
	    num=num//10
	for i in range(0,len(arr)):
		if(arr[i]%2==1):
			sum=sum+arr[i]
		else:
			continue
	if(sum%2==0):
		print("E")
	else:
		print("O")
except ValueError:
	print("invalid")
