try:
	base,height=map(int,input().split())
	print(int(0.5*base*height))
except ValueError:
	print("invalid")