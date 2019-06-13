str1=input()
str2=input()
astr=str1+str2
count=1
for i in astr:
	if astr.count(i)==1:
		count=1
	else:
		count=0
if count==1 and len(astr)==26:
	print("complementary")
else:
	print("non-complementary")