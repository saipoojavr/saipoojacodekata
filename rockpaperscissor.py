ch1,ch2=input().split()
if(ch1=="R" and ch2=="P") or (ch1=="P" and ch2=="R"):
	print("P")
elif(ch1=="P" and ch2=="S") or (ch1=="S" and ch2=="P"):
	print("S")
elif(ch1=="S" and ch2=="R") or (ch1=="R" and ch2=="S"):
	print("R")
elif(ch1==ch2):
	print("D")