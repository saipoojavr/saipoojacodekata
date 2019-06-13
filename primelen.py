astr=input()
count=0
for i in range(0,len(astr)):
	if(astr[i]!=" "):
		count+=1
if count > 1: 
	   for iter in range(2, count//2): 
	       if (count % iter) == 0: 
	           print("no") 
	           break
	   else: 
	       print("yes") 
else:
	print("no") 