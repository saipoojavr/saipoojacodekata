sent=input()
count=len(sent)
sp=0
for iter in range(0,count):
	if(sent[iter].isdigit()==True):
		sp=sp+1
	else:
		continue
print(sp)