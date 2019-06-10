try:
	n1,n2=map(int,input().split())
	num=n1*n2
	con=bin(num)[2::]
	for i in range(-1,-len(con)-1,-1):
		if(con[i]=="1"):
			break
	print(-(i))
except ValueError:
	print("invalid")