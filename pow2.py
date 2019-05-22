try:
	num=int(input())
	key=num
	temp=0
	while num>1:
	    if num%2==0:
	        num=num/2
	        temp=temp+1
	    else:
	        print("no")
	        break
	if (2**temp)==key:
	    print("yes")
except ValueError:
    print("invalid")