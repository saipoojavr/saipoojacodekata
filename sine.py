import math
try:
	angle=int(input())
	radian=angle*(math.pi/180)
	if radian<1 and radian>0:
		print(round(math.sin(radian),1))
	else:
		print(round(math.sin(radian)))
except ValueError:
	print("invalid")