try:	
	num=int(input())
	con=bin(num)[2::]
	for i in range(-1,-len(con)-1,-1):
		if(con[i]=="1"):
			break
	print(-(i))
except ValueError:
	print("invalid")
			
