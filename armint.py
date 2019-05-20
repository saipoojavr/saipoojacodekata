try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	for iter in range(num1+1,num2):
		add = 0  
		tempo = iter  
		while tempo > 0:  
		   digit = tempo % 10  
		   add += digit ** 3  
		   tempo //= 10  
		if iter == add:  
		   print(iter,end=" ")  
		else:  
		   continue
except ValueError:
	print("invalid")