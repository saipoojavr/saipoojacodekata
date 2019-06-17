str1,str2=input().split()
a=len(str1)
b=len(str2)
c=a%b
d=b%a
if b==a+1 or a==b+1:
	print("yes")
elif c==0 and d==0 :
	print("no")
else:
	print("no")