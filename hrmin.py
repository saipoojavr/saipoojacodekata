try:
	mini=int(input())
	print(mini//60,mini%60)
except ValueError:
	print("invalid")