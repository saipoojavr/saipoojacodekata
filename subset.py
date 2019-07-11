try:
	n1,n2=map(int,input().split())
	a1=set(map(int,input().split()))
	a2=set(map(int,input().split()))
	if a2.issubset(a1):
		print("YES")
	else:
		print("NO")
except ValueError:
	print("invalid")
	