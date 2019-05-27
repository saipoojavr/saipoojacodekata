word1,word2=map(str,input().split())
count=0
for iter in range(0,len(word1)):
	if word1[iter]!=word2[iter]:
		count=count+1
	else:
		continue
if count==1:
	print("yes")
else:
	print("no")
