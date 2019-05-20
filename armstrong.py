try:
	number = int(input())  
	add = 0  
	tempo = number  
	while tempo > 0:  
	   digit = tempo % 10  
	   add += digit ** 3  
	   tempo //= 10  
	if number == add:  
	   print("yes")  
	else:  
	   print("no")
except ValueError:
	print("invalid")