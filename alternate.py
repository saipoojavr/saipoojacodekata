word1=input()
word1=list(word1)
for iter in range(0,len(word1),2):
	word1[iter],word1[iter+1]=word1[iter+1],word1[iter]
print(''.join(word1))