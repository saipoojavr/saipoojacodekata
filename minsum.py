try:	
	num=int(input())
	arr=[int(x) for x in input().split()]
	s=[0]
	for i in range(num):
	    for j in range(i,num):
	        c=arr[i:j+1]
	        s.append(sum(c))
	print(min(s))
except ValueError:
	print("invalid")