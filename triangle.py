import math
try:
	ang1,ang2,ang3=map(int,input().split())
	if((ang1+ang2+ang3)==180 and ang1!=0 and ang2!=0 and ang3!=0):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")