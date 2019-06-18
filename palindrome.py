str1=input()
k=len(str1)
count=0
if(k%2==1):
	for i in range(0,k//2-1):
		if(str1[i]!=str1[k-i-1]):
			count+=1
else:
	for i in range(0,k//2):
		if(str1[i]!=str1[k-i-1]):
			count+=1
if(count<=1):
	print("yes")
else:
	print("no")