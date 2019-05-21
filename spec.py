sent=input()
count=len(sent)
sp=0
for iter in range(0,count):
	if(sent[iter].isdigit()==True):
		continue
	elif(sent[iter].isalpha()==True):
		continue
	elif(sent[iter]==" "):
		continue
	else:
		sp=sp+1
print(sp)