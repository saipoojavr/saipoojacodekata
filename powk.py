try:
	num,num1=map(int,input().split())
	key=num
	temp=0
	while num>1:
	    if num%num1==0:
	        num=num/num1
	        temp=temp+1
	    else:
	        print("no")
	        break
	if (num1**temp)==key:
	    print("yes")
except ValueError:
    print("invalid")