astr=input()
count1=0
count2=0
for iter in range(0,len(astr)):
	if(astr[iter]=='('):
		count1+=1
	elif(astr[iter]==')'):
		count2+=1
if(count1==count2):
	print("yes")
else:
	print("no")