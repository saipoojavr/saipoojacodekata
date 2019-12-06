s=input()
n=len(s)
for i in range(0,n):
	for j in range(0,n):
		if((i==j) or (i+j==n-1)):
			print(s[i],end="")
		else:
			print(" ",end="")
	print("\r")