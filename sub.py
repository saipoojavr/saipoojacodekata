try:
	hr1,min1=map(int,input().split())
	hr2,min2=map(int,input().split())
	hr3=abs(hr1-hr2)
	min3=abs(min1-min2)
	print(hr3,min3)
except ValueError:
	print("invalid")
	
