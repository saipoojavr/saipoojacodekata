try:
	num=int(input())
	a=1
	b=1
	if(num==1):
	    print(a,end='')
	if(num>1):
	    for count in range(0,num):
	        if(count==num-1):
	            print(a,end='')
	        else:
	            print(a,end=' ')
	        nth=a+b
	        a=b
	        b=nth
except ValueError:
	print("invalid")
		