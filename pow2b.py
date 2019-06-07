try:
	num2=int(input())
	key=num2
	temp=0
	while num2>1:
	    if num2%2==0:
	        num2=num2/2
	        temp=temp+1
	    else:
	        print("no")
	        break
	if (2**temp)==key:
	    print("yes")
except ValueError:
    print("invalid")
