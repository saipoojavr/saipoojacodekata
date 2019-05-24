ach=str(input())
l=len(ach)
for i in range(0,l):
	if(i%2==0):
		print(ach[i],end="")
print(end=" ")
for i in range(0,l):
	if(i%2==1):
		print(ach[i],end="")
		