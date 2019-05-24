try:
	leng,bre,hei=map(int,input().split())
	tsa=2*(leng*bre+bre*hei+hei*leng)
	vol=leng*bre*hei
	print(tsa,end=" ")
	print(vol)
except ValueError:
	print("invalid")