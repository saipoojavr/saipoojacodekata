astr=input()
count=0
l=len(astr)
for i in range(0,l-1):
    for j in range(i+1,l):
        if astr[i]==astr[j]:
            count=count+1
if count==0:
    print("Yes")
else: 
	print("No")