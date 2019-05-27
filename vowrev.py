length=int(input())
astr=str(input())
for i in range(-1,-length-1,-1):
	if not(astr[i]=='a' or astr[i]=='e' or astr[i]=='i' or astr[i]=='o' or astr[i]=='u'):
		print(astr[i],end="")

