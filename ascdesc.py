try:	
	num=int(input())
	arr=list(map(int,input().split()))
	if num%2!=0:
	    mid=(num-1)//2
	    a=sorted(arr[0:mid])
	    b=sorted(arr[mid:])
	    c=a+b[::-1]
	    print(*c)
	else:
	    mid=num//2
	    a=sorted(arr[0:mid])
	    b=sorted(arr[mid:])
	    c=a+b[::-1]
	    print(*c)
except ValueError:
	print("invalid")