try:
	M2=int(input())
	l2=list(map(int,input().split()))
	for i2 in range(0,M2-2):
	    for j2 in range(i2+1,M2-1):
	        for k2 in range(j2+1,M2):
	            if(l2[i2]+l2[j2]==l2[k2]):
	                print(l2[i2], l2[j2], l2[k2])
except ValueError:
	print("invalid")
