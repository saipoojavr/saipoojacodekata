n=int(input())
for i in range(0,n):
	for j in range(0,n-i-1):
		print(" ",end="")
	
	for l in range(i,-1,-1):
		print(l+1,end="")
	for m in range(2,i+2):
		print(m,end="")
	print("\r")
for i in range(n-2,-1,-1):
	for j in range(0,n-i-1):
		print(" ",end="")
	
	for l in range(i,-1,-1):
		print(l+1,end="")
	for m in range(2,i+2):
		print(m,end="")
	print("\r")